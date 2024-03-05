from email_sender import send_email
from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/b8e3551c304b5ac65a4a").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        contact_data = request.form
        print(contact_data)
        name = contact_data["name"]
        email = contact_data["email"]
        phone_number = contact_data["phone"]
        message = contact_data["message"]
        print(f'{name}\n{email}\n{phone_number}\n{message}')
        send_email(name=name, email=email, phone_number=phone_number, message=message)
        # receive_data()
        # Change some things on the contact page depending on if this is a post method or a get method
        return render_template("contact.html", after_post=True)
    return render_template("contact.html", after_post=False)


# @app.route("/form-entry", methods=["POST"])
def receive_data():
    contact_data = request.form
    print(contact_data)
    name = contact_data["name"]
    email = contact_data["email"]
    phone_number = contact_data["phone"]
    message = contact_data["message"]
    print(f'{name}\n{email}\n{phone_number}\n{message}')
    return (f"<h1>"
            f"Successfully sent your message "
            f"{name}!"
            f"</h1>")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
