from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length
import os
from flask_bootstrap import Bootstrap5

admin_email = "admin@email.com"
admin_password = "12345678"


class MyForm(FlaskForm):
    email = StringField(label='Email:', validators=[DataRequired(), validators.Email()])
    password = PasswordField(label='Password:',
                             validators=[DataRequired(), Length(min=3, max=11, message="Enter at least 8 characters")])
    submit = SubmitField(label='Log in')


app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    # form.validate_on_submit()
    # If the validation was successful, check the data
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        if form.email.data == admin_email and form.password.data == admin_password:
            # If the data matches the checked email and password, go to the success page
            return render_template('success.html')
        else:
            # Any other valid data goes to denied page instead of back to login page
            return render_template('denied.html')
    # print(form.email)
    # print(form.password)
    # If the form wasn't validated, send the same page again
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
