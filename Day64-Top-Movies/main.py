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
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
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



if __name__ == '__main__':
    app.run(debug=True)
