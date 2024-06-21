# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
# # cursor.execute(
# #     "CREATE TABLE books ("
# #     "id INTEGER PRIMARY KEY, "
# #     "title varchar(250) NOT NULL UNIQUE, "
# #     "author varchar(250) NOT NULL, "
# #     "rating FLOAT NOT NULL"
# #     ")")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# Using SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask import Flask

app = Flask(__name__)

# TODO:
# Initialize the db object ✔️
# Define the model✔️
# Create the table✔️
# Create a entry to the table ✔️


# Initialize the db object
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)

db.init_app(app)

# Define the model
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# Create the table
with app.app_context():
    db.create_all()

# Create an entry to the table
with app.app_context():
    try:
        new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
        db.session.add(new_book)
        db.session.commit()
    except:
        pass

# Read all entries
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    print(all_books)
