from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        form_data = request.form
        # print(form_data)
        # print(form_data["Name"])
        book = {
            "title": form_data["title"],
            "author": form_data["author"],
            "rating": form_data["rating"]
        }
        all_books.append(book)
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

