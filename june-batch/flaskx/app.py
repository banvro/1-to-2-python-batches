from flask import Flask
from flask import render_template, request
import mysql.connector

app = Flask(__name__)
conwc = mysql.connector.connect(host = "localhost", user = "root", password = "1234", database = "test", auth_plugin='mysql_native_password')
couser = conwc.cursor()

@app.route('/')
def xyz():
    return "hello website.."

@app.route('/about')
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
        print(uname, age)
        couser.execute(f'insert into hlo values("{uname}", {age})')
        conwc.commit()
        # user = request.form['usernmae']

        return f"usernae is {uname} and user age is {age}"

@app.route("/show")
def showdata():
    couser.execute('select * from hlo')
    data = couser.fetchall()
    return render_template("show.html", data = data)

@app.route("/showupdate/<int:id>")
def updateshow(id):
    couser.execute(f'select * from hlo where id = {id}')
    data = couser.fetchone()
    return render_template("update.html", data = data)



if __name__ == "__main__":
    app.run(debug = True) 