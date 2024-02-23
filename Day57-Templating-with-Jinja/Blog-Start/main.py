import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/blog/<int:num>')
def show_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    current_post = all_posts[num-1]
    return render_template("post.html", post=current_post)


if __name__ == "__main__":
    app.run(debug=True)
