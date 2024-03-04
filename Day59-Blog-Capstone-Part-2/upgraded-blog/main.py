import requests
from flask import Flask, render_template


def get_post_data():
    # Make a request to the api from npoint to get our json data
    response = requests.get(url="https://api.npoint.io/b8e3551c304b5ac65a4a")
    response.raise_for_status()
    data = response.json()
    print(data)
    return data


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blogs=blog_data)


@app.route("/<int:blog_id>")
def see_blogs(blog_id):
    # blog_id = 1-1
    # print(blog_id)
    img = "post-bg.jpg"
    if blog_id == 1:
        img = "thomas-verbruggen-5A06OWU6Wuc-unsplash.jpg"
    elif blog_id == 2:
        img = "priscilla-du-preez-dOnEFhQ7ojs-unsplash.jpg"
    elif blog_id == 3:
        img = "e_i9-TQWqt61BofA-unsplash.jpg"
    # Decrease the blog id by 1, so it can directly have the right index in the blog_data array
    blog_id = blog_id-1
    return render_template("post.html", blogs=blog_data, id=blog_id, img=img)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    blog_data = get_post_data()
    app.run(debug=True)

