from flask import Flask

# __name__ is a special attribute built into python, and it gives the
# current class, function, method, descriptor, or generator instance
app = Flask(__name__)


@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>Home page</p>'
            '<img src='
            '"https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcG5xMm5rejEwcG1tejB4dzZ0M3ViZ3p6bmhodmRtbDU3MDdneGZzNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ddAGR2jh0FDoY/giphy.gif"'
            'width=300>')


@app.route("/bye")
def say_bye():
    return "Bye"


# Take in data from the url as a parameter
# @app.route("/username/<name>")
# This can also be used to get specific arguments from the url
# @app.route("/username/<path:name>")
# this gives everything after /username to save as name
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


# Create a decorator to bold the display text
def make_bold(function):
    # The decorator needs to take the return of the function and apply bold to it
    # So this is what it looks like without the cleaner way of using a decorator
    bold = function()
    print(f"<b>{bold}</b>")


def make_bold_decorator(function):
    def wrapper_function():
        # text = function()
        # return f"<b>{text}</b>"
        # Apply bold to everything in the return of the function
        return f"<b>{function()}</b>"
    # return the wrapper_function without parenthesis, so we return the function itself and not the function call
    return wrapper_function


def make_italics_decorator(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underlined_decorator(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route("/exercise1")
@make_bold_decorator
@make_italics_decorator
@make_underlined_decorator
def message():
    # print("Message")
    return "Message!"


if __name__ == "__main__":
    # debug mode allows the auto-reloading and gives the Flask debug view
    app.run(debug=True)
    # message()
    # make_bold(message)
