from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Float, String


class Base(DeclarativeBase):
    # This is part of initializing the db object
    pass


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
# initialize the db object
db = SQLAlchemy(model_class=Base)
# Initialize the app with the extension
db.init_app(app)


# all_books = []


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# Create the table
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # Get all books and sort by book title
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # put the result in all_books
    all_books = result.scalars().all()
    print(all_books)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        form_data = request.form
        # print(form_data)
        # print(form_data["Name"])
        # book = {
        #     "title": form_data["title"],
        #     "author": form_data["author"],
        #     "rating": form_data["rating"]
        # }
        # all_books.append(book)

        # Add the new book into the table
        with app.app_context():
            # Create a new instance of the book class
            new_book = Book(title=form_data["title"], author=form_data["author"], rating=form_data["rating"])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO: Finish this part next
    if request.method == "POST":
        # Use the book id to find the book info in the db
        # book = book_id
        book_id = request.form["id"]
        # book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        book = db.get_or_404(Book, book_id)
        book.rating = request.form["rating"]
        db.session.commit()
        # return render_template("edit.html", book=book)
        return redirect(url_for('home'))
    book_id = request.args.get("id")
    book = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book)


if __name__ == "__main__":
    app.run(debug=True)
