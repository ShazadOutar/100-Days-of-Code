from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
# add in the login manager from flask_login
login_manager = LoginManager()
# add it to the app
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # get the user with the matching user id and return none if there is no match
    user = db.session.get(User, user_id)
    return user


# CREATE DATABASE

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB

# add in the UserMixin from flask_login as part of our User object
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))




with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the email entered is already saved in the db
        # query = db.session.query(db.exists().where(User.email == request.form.get("email"))).scalar()
        result = db.session.execute(db.select(User).where(User.email == request.form.get("email")))
        query = result.scalar()
        # query returns none if there was no row found with the same email as the input email
        print(query)
        if query:
            flash("Email in use, please log in instead")
            return redirect("login")
        else:
            hash_and_salted_password = generate_password_hash(
                request.form.get('password'),
                method='pbkdf2:sha256',
                salt_length=8
            )
            new_user = User(
                email=request.form.get('email'),
                name=request.form.get('name'),
                password=hash_and_salted_password,
            )

            db.session.add(new_user)
            db.session.commit()

            # Log in and authenticate user after adding details to database.
            login_user(new_user)

            # Can redirect() and get name from the current_user
            return redirect(url_for("secrets"))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    # check if the email is found in the database
    # print(request.form.get("email"))
    if request.method == "POST":
        # print(request.form.get("email"))
        # All emails saved are unique so we just need to find a match
        result = db.session.execute(db.select(User).where(User.email == request.form.get("email")))
        user = result.scalar()

        if user:
            # the email did find a match in the db, then check the password
            # print(request.form.get("password"))
            # check the input password against the password saved in the db
            # use the check password hash function
            if check_password_hash(pwhash=user.password, password=request.form.get("password")):
                print("Matched")
                # the user email was found and the password is right,
                # - sign the user in
                if login_user(user=user):
                    print("logged in")
                else:
                    print("Didn't work")
                # - go to the secrets page
                return redirect(url_for("secrets"))
                # return render_template("secrets.html", name=user.name)
            else:
                print("Incorrect password")
                flash("Incorrect password")
                return render_template("login.html")
        else:
            # if the email did not find a match, then tell them they need to sign up
            print("User email not found")
            flash("That email is not registered, please try again")
            return render_template("login.html")

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    # You can get user info from flask login tools
    print(current_user.name)
    return render_template("secrets.html")


@app.route('/logout')
# log out the user and return to the home page
def logout():
    logout_user()
    # return render_template("index.html")
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    path = "files/cheat_sheet.pdf"
    return send_from_directory(directory="static", path=path)


if __name__ == "__main__":
    app.run(debug=True)
