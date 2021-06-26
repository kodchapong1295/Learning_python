from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media2.giphy.com/media/K1tgb1IUeBOgw/giphy.gif?cid=ecf05e47jy02icf5ac8qtvbli96j666j8vg3b4hjxtd58e39&rid=giphy.gif&ct=g">'

@app.route('/bye')
def say_bye():
    return 'Bye'

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)