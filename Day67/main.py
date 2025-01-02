from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# Add Blog Form
class BlogForm(FlaskForm):
    title = StringField('Title')
    subtitle = StringField('Subtitle')
    # date = DateField('Date')
    author = StringField('Author')
    img_url = URLField('Background Image URL')
    body = CKEditorField('Body')
    submit = SubmitField('Submit')

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    blog_posts = db.session.query(BlogPost).all()
    # print(blog_posts)
    # Add each blog to the posts list
    for blog in blog_posts:
        posts.append(blog)
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    # requested_post = "Grab the post from your database"
    # print(post_id)
    requested_post = db.session.get(BlogPost, post_id)
    if requested_post:
        return render_template("post.html", post=requested_post)
    else:
        return "<h1>Page Not Found<h1>"

# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def create_new_post():
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            date = date.strftime(date.today(), "%m/%d/%Y"),
            body = form.body.data,
            author = form.author.data,
            img_url = form.img_url.data,
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "PATCH"])
def edit_post(post_id):
    # requested_post = db.session.get(BlogPost, post_id)
    # print(requested_post.title)
    # return render_template("post.html", post=requested_post)
    post = db.session.get(BlogPost, post_id)
    edit_form = BlogForm()  
    return render_template("make-post.html", form=edit_form, is_edit=True)

# TODO: delete_post() to remove a blog post from the database

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
