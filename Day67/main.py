from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.fields.simple import URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date, datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

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

class BlogForm(FlaskForm):
    title = StringField("Title", [validators.DataRequired()])
    subtitle = StringField("Subtitle", [validators.DataRequired()])
    author_name = StringField("Your Name", [validators.DataRequired()])
    img_url = URLField("Image URL", [validators.DataRequired()])
    content = CKEditorField("Blog Content", [validators.DataRequired()])
    submit = SubmitField("Submit Post")


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    # print(db.session.query(BlogPost).all()[0].id)
    blogs = db.session.query(BlogPost).all()
    posts = []
    for blog in blogs:
        posts.append(blog)
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.get(BlogPost, {"id": post_id})
    if requested_post:
        return render_template("post.html", post=requested_post)
    else:
        return "<h1>Page Not Found</h1>"

# TODO: add_new_post() to create a new blog post
@app.route('/new_post', methods=["GET", "POST"])
def add_new_post():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        current_date = datetime.now()
        blog_date = current_date.strftime("%B %d, %Y")
        # blog_form.title.data = blog_date
        new_blog_post = BlogPost(
            title = blog_form.title.data,
            subtitle = blog_form.subtitle.data,
            date = blog_date,
            body = blog_form.content.data,
            author = blog_form.author_name.data,
            img_url = blog_form.img_url.data
        )
        db.session.add(new_blog_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=blog_form)



# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    # blog_data = db.session.get(BlogPost, post_id)
    blog_data = db.get_or_404(BlogPost, post_id)
    blog_form = BlogForm(
        title = blog_data.title,
        subtitle = blog_data.subtitle,
        author_name = blog_data.author,
        img_url = blog_data.img_url,
        content = blog_data.body
    )
    if blog_form.validate_on_submit():
        blog_data.title = blog_form.title.data
        blog_data.subtitle = blog_form.subtitle.data
        blog_data.date = blog_data.date
        blog_data.body = blog_form.content.data
        blog_data.author = blog_form.author_name.data
        blog_data.img_url = blog_form.img_url.data
        db.session.commit()

        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=blog_form, is_edit=True)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<post_id>")
def delete_post(post_id):
    db.session.query(BlogPost).filter(BlogPost.id == post_id).delete()
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
