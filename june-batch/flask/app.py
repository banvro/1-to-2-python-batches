from flask import Flask
from flask import render_template, request, redirect

import mysql.connector


conn = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "xyz")

curser = conn.cursor()







app = Flask(__name__)

@app.route('/')
def xyz():
    return "hello website.."

@app.route('/abouts')
def aboutus():
    return "this is my about page....."

@app.route('/show/<int:id>')
def showthis(id):
    print(id)
    # return render_template('abc.html')
    return f"my id is {id}"


@app.route('/xyz')
def showthiss():
    return render_template('myfrom.html')

@app.route('/send_data', methods = ['post', ])
def savedata():
    if request.method == "POST":
        uname = request.form.get('usernmae')
        age = request.form.get('age')
        # print(uname, age)
        curser.execute(f"insert into mytable values('{uname}', {age})")
        conn.commit()

        return redirect("xyz")
        # user = request.form['usernmae']

        return f"usernae is {uname} and user age is {age}"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug = True) 