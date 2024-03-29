from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, ValidationError
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps (URL)', validators= [URL()])
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating',
                                choices=[
                                         '✘',
                                         '☕️☕️☕️☕️☕️',
                                         '☕️☕️☕️☕️',
                                         '☕️☕️☕️',
                                         '☕️☕️',
                                         '☕️'],
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating',
                              choices=[
                                       '✘',
                                       '💪💪💪💪💪',
                                       '💪💪💪💪',
                                       '💪💪💪',
                                       '💪💪',
                                       '💪'],
                              validators=[DataRequired()])
    power = SelectField('Power Socket Availability',
                        choices=[
                                '✘',
                                '🔌🔌🔌🔌🔌',
                                '🔌🔌🔌🔌',
                                '🔌🔌🔌',
                                '🔌🔌',
                                '🔌'],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("New Cafe Added.")
        with open('cafe-data.csv', mode='a', encoding="utf8") as csv_file:
            new_row = f"\n{form.cafe.data}," \
                      f"{form.cafe_location.data}," \
                      f"{form.opening_time.data}," \
                      f"{form.closing_time.data}," \
                      f"{form.coffee_rating.data}," \
                      f"{form.wifi_rating.data}" \
                      f",{form.power.data}"
            csv_file.write(new_row)
        csv_file.close()
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes', methods=['GET', 'POST'])
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
