from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    form_data = request.form
    print(form_data)
    # return render_template("login.html", form=form_data)
    username = form_data["username"]
    password = form_data["password"]
    return (f'<h1>'
            f'Username: {username},'
            f'Password: {password}'
            f' </h1>')


if __name__ == "__main__":
    app.run(debug=True)
