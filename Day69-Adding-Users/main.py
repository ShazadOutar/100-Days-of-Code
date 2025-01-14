from datetime import date

from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.validators import email

# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    user = db.session.get(User, user_id)
    return user

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # create Foreign key "users.id" which refers to the table User's name
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    # create a reference to the User Object, "posts" refers to the posts property in the User class
    author = relationship("User", back_populates="posts")

    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    posts = relationship("BlogPost", back_populates="author")


with app.app_context():
    db.create_all()

#Create admin-only decorator
def admin_only(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        # if the current user is 1, they are the admin and have permission to do this
        if current_user.id == 1:
            return function(*args, **kwargs)
        # everyone else does not have permission
        else:
            return abort(403)
    return decorated_function


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # when the form is submitted, then try to add the user
        # first check if the email is a new email or if it's already been registered already
        query = db.session.execute(db.select(User).where(User.email == form.email.data))
        matched_user = query.scalar()
        # if a match was found
        if matched_user:
            # flash the warning message and redirect them to login instead
            flash("You're already registered with that email, try to log in instead")
            return redirect(url_for('login'))

        # encrypt their password
        password = generate_password_hash(
            password=form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        # create a new User object from the form data
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=password
        )
        # add in the user to the db
        db.session.add(new_user)
        db.session.commit()

        # login the user with Flask Login
        login_user(user=new_user)

        return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form)



@app.route('/login', methods=["GET", "POST"])
def login():
    # create the login form
    form = LoginForm()
    # if the form was submitted, then process the log in
    if form.validate_on_submit():
        # search for the users email in the db
        query = db.session.execute(db.select(User).where(User.email == form.email.data))
        matched_user = query.scalar()
        # print(query.scalar().email)
        if matched_user:
            # if there was a match found for the email address entered
            # then check if their password matches the saved password
            if check_password_hash(password=form.password.data, pwhash=matched_user.password):
                # then we sign them in and put them on the get all posts page
                # print("Correct Password")
                login_user(matched_user)
                return redirect(url_for('get_all_posts'))
            else:
                flash("Incorrect Password")
                return redirect(url_for('login'))
                # print("Incorrect Password")
        else:
            # print("No match")
            flash("Email Address Not Found")
            return redirect(url_for('login'))
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    print("Logged out")
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    if current_user.is_authenticated:
        print(current_user.name)
    else:
        print("Not logged in")
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
# @admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            # author=current_user.name,
            author=User(name=current_user.name),
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)



@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
