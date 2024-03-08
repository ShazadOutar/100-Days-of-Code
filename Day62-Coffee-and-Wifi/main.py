import wtforms.validators
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap5(app)


class CafeForm(FlaskForm):
    coffee_rating = [('1', '🍵'), ('2', '🍵🍵'), ('3', '🍵🍵🍵'), ('4', '🍵🍵🍵🍵'), ('5', '🍵🍵🍵🍵🍵')]
    wifi_rating = [('0', '✖️'), ('1', '🦾'), ('2', '🦾🦾'), ('3', '🦾🦾🦾'), ('4', '🦾🦾🦾🦾')]
    power_rating = [('0', '✖️'), ('1', '🔌'), ('2', '🔌🔌'), ('3', '🔌🔌🔌'), ('4', '🔌🔌🔌🔌')]

    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)',
                           validators=[DataRequired(), wtforms.validators.URL(message="Please enter a valid URL")])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffee = SelectField('Coffee', validators=[DataRequired()], choices=coffee_rating)
    wifi = SelectField('Wifi Strenght', validators=[DataRequired()], choices=wifi_rating)
    power = SelectField('Power Socket Availability', validators=[DataRequired()], choices=power_rating)
    submit = SubmitField('Submit')


def add_form_data(input_form_data_list):
    # Use the data from the form to add to the csv file
    with open(file="cafe-data.csv", mode='a', encoding='utf-8') as file:
        file.write('\n')
        input_string = "\n"
        for item in input_form_data_list:
            # input_string + str(item)
        file.write(input_form_data_list)



# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # if the form data passes the validators, add it to the csv file
        print("True")
        form_data = [
            form.cafe, form.location, form.open, form.close, form.coffee, form.wifi, form.power]
        add_form_data(form_data)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
    # form_data = "Ginger & White,https://goo.gl/maps/DqMx2g5LiAqv3pJQ9,7:30AM,5:30PM,☕☕☕,✘,🔌"
    # add_form_data(form_data)
