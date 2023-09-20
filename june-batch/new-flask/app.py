# pip install flask

from flask import Flask, render_template, request, redirect
import mysql.connector


conn = mysql.connector.connect(host="localhost", username= "root", password="1234", database="flasktable")

curser = conn.cursor()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/savedata", methods = ["post"])
def savedata():
    if request.method == "POST":
        name = request.form.get("name")
        number = request.form.get("number")
        email = request.form.get("email")
        dec = request.form.get("dec")

        # print(name, number, email, dec)
        curser.execute(f"insert into flasktables values('{name}', {number},'{email}', '{dec}')")
        conn.commit()
        return redirect("/show")
    return "save data"
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/show")
def show():
    curser.execute("select * from flasktables")
    data = curser.fetchall()
    return render_template("show.html", mydata = data)

@app.route("/delete/<xyz>", methods = ["POST",])
def deletethis(xyz):
    if request.method == "POST":
        curser.execute(f"delete from flasktables where Name = '{xyz}'")
        return redirect("/show")








if __name__ == "__main__":
    app.run(debug = True, port = 1000)
