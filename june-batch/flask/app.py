from flask import Flask
from flask import render_template, request
app = Flask(__name__)

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
        # user = request.form['usernmae']

        return f"usernae is {uname} and user age is {age}"

    



if __name__ == "__main__":
    app.run(debug = True) 