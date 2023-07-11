from flask import Flask, render_template, request
app = Flask (__name__)

@app.route ('/')
def index():
    render_template ('base.html')
    return render_template ('index.html')




def HasUpperCase(string):
    for letter in string:
        if letter.isupper():
            return True
        
def HasLowerCase(string):
    for letter in string:
        if letter.islower():
            return True
        
def HasNumAtEnd(string):
    if string[-1].isnumeric():
        return True

@app.route ('/Report')
def give_report():
    username = request.args.get("username")
    password = request.args.get("password")

    Details = "Your password passed the requirements!"
    listItem1 = ""
    listItem2 = ""
    listItem3 = ""

    success = True

    if not HasUpperCase(username) or not HasUpperCase(password):
        success = False

        item = "Must have an upper case letter somewhere"
        if listItem1 == "":
            listItem1 = item
        elif listItem2 == "":
            listItem2 = item
        else:
            listItem3 = item
    if not HasLowerCase(username) or not HasLowerCase(password):
        success = False
        item = "Must have a lower case letter somewhere"
        if listItem1 == "":
            listItem1 = item
        elif listItem2 == "":
            listItem2 = item
        else:
            listItem3 = item
    if not HasNumAtEnd(username) or not HasNumAtEnd(password):
        success = False
        item = "Must contain a number at the end"
        if listItem1 == "":
            listItem1 = item
        elif listItem2 == "":
            listItem2 = item
        else:
            listItem3 = item


    if not success:
        Details = "Your password failed for these reasons:"

    print(listItem1)
    print(listItem2)
    print(listItem3)

    return render_template (
        'report.html', 
        Details=Details,
        listItem1=listItem1,
        listItem2=listItem2,
        listItem3=listItem3
    )

if __name__ == '__main__':
    app.run()