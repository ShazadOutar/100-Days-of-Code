import os
import sqlite3

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

MOVIE_API_KEY = os.environ["MOVIE_API_KEY"]

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# creates the db in the instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-ten-movies.db"
Bootstrap5(app)


# CREATE DB

# To create it with sqlite
# db = sqlite3.connect("top-10-movies.db")
# cursor = db.cursor()

# To create it with sqlalchemy
class Base(DeclarativeBase):
    # this is used for initializing the db object
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE

# Define the table model
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# Create the table
with app.app_context():
    db.create_all()


# Add starting movies to the db
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     # db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    # get all the movies and sort them by rank
    all_movies_query = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies_list = all_movies_query.scalars().all()
    return render_template("index.html", movies=all_movies_list)


class EditForm(FlaskForm):
    rating = FloatField(label="Update your rating:", validators=[
        DataRequired(message="Please do not leave empty")
    ])
    review = StringField(label="Update your review:", validators=[
        DataRequired(message="Please do not leave empty")
    ])
    submit = SubmitField(label="Submit")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    # get the movie id for the movie being edited
    movie_id = request.args.get("id")
    form = EditForm()
    if request.method == "POST" and form.validate_on_submit():
        rating = form.rating.data
        review = form.review.data

        movie_to_update = db.get_or_404(Movie, movie_id)
        # movie_to_update.ranking = request.form["ranking"]
        movie_to_update.review = review
        # movie_to_update.rating = request.form["rating"]
        movie_to_update.rating = rating
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=form, id=movie_id)


@app.route("/delete", methods=["GET"])
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title:", validators=[
        DataRequired(message="Please do not leave empty")
    ])
    submit = SubmitField(label="Add Movie")


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if request.method == "POST" and form.validate_on_submit():
        # get the results of the search from the movie api
        params = {
            "query": form.title.data,
            "include_adult": False,
            "language": "en-US",
            "api_key": MOVIE_API_KEY
        }
        print(params)
        headers = {
            "accept": "application/json",
            # "Authorization": "Bearer " + MOVIE_API_KEY
        }

        # url = ("https://api.themoviedb.org/3/search/movie?"
        #        "query=The%20Matrix&include_adult=false&language=en-US&page=1")
        url = "https://api.themoviedb.org/3/search/movie"
        response = requests.get(url, headers=headers, params=params)
        # print(response)
        # print(response.text)
        # print(response.json())
        movies_search_results_json = response.json()["results"]
        print(movies_search_results_json)
        return render_template('select.html', movies=movies_search_results_json)

    return render_template("add.html", form=form)


def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        # "movie_id": movie_id,
        "language": "en-US",
        "api_key": MOVIE_API_KEY,
    }
    headers = {
        "accept": "application/json",
    }
    response = requests.get(url, params=params, headers=headers)
    print(response.json())
    response_json = response.json()
    title = response_json["original_title"]
    print(title)
    # title = response.json()["original_title"]
    # print(title)
    # movie_data = {
    #     "title": response_json["original_title"],
    #     "img_url": response_json["poster_path"],
    #     "year": response_json["release_date"],
    #     "description": response_json["overview"]
    # }

    # Add this to get the images to work
    base_url = "https://api.themoviedb.org/3/configuration"
    params = {
        "api_key": MOVIE_API_KEY
    }
    headers = {
        "accept": "application/json",
    }

    img_response = requests.get(base_url, headers=headers, params=params)
    print(img_response.json()["images"])
    img_url = f'{img_response.json()["images"]["base_url"]}/w500/{response_json["poster_path"]}'

    movie_data = Movie(
        title=response_json["original_title"],
        # img_url=response_json["poster_path"],
        img_url=img_url,
        year=response_json["release_date"],
        description=response_json["overview"],
        rating=0,
        ranking=0,
        review=""
    )
    print(movie_data)
    return movie_data


@app.route('/find')
def find():
    # search the movie name up to get its ID
    movie_id = request.args.get("movie_id")
    print(movie_id)
    # Get the details of that movie from the API
    # new_movie = get_movie_details(movie_id)
    with app.app_context():
        new_movie = get_movie_details(movie_id)
        db.session.add(new_movie)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
