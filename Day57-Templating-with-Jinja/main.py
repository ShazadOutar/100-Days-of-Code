from random import randint
import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)


def get_guess_age(name):
    query = {"name": name}
    response = requests.get("https://api.agify.io/", params=query)
    response.raise_for_status()
    print(response)
    data = response.json()

    print(data)
    return data["age"]


def get_guess_gender(name):
    query = {"name": name}
    response = requests.get("https://api.genderize.io", params=query)
    response.raise_for_status()
    print(response)
    data = response.json()

    print(data)
    return data["gender"]


@app.route("/")
def home():
    random_number = randint(1, 10)
    current_year = datetime.date.today().year
    # print(current_year)
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def name_guess(name):
    age_guess = get_guess_age(name)
    gender_guess = get_guess_gender(name)
    return render_template("name_guess_info.html", name=name, gender=gender_guess, age=age_guess)


@app.route("/blog/<int:num>")
def blog_function(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)
