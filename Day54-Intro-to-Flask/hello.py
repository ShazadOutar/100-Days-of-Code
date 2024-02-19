from flask import Flask

# __name__ is a special attribute built into python, and it gives the
# current class, function, method, descriptor, or generator instance
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run()
