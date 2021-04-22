from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
import datetime

TMDB_KEY = os.environ['TMDB_KEY']
TMDB_URL = "https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# db.session.add(new_movie)
# db.session.commit()


class EditForm(FlaskForm):
    new_rating = StringField("Your Rating Out of 10 e.g 7.5", validators=[DataRequired()])
    new_review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    # This line loops through all the movies
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    edit_form = EditForm()
    movie_id = request.args.get('id')
    movie_to_update = Movie.query.get(movie_id)

    if edit_form.validate_on_submit():

        movie_to_update.rating = edit_form.new_rating.data
        movie_to_update.review = edit_form.new_review.data
        db.session.commit()

        return redirect(url_for('home'))
    else:
        return render_template('edit.html', movie=movie_to_update, form=edit_form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


searched_movies = []


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()

    if add_form.validate_on_submit():

        parameters = {
            "api_key": TMDB_KEY,
            "query": add_form.title.data
        }

        search_results = requests.get(url=TMDB_URL, params=parameters).json()['results']
        for search_result in search_results:
            movie_id = search_result['id']

            parameters = {
                "api_key": TMDB_KEY
            }
            movie_details = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}", params=parameters).json()
            movie = {
                "id": movie_id,
                "title": movie_details["title"],
                "description": movie_details["overview"],
                "year": (movie_details["release_date"]).split('-')[0],
                "img_url": movie_details["poster_path"],
                "rating": movie_details["vote_average"]
            }

            searched_movies.append(movie)
        return redirect(url_for('select'))
    else:
        return render_template('add.html', form=add_form)


@app.route('/select', methods=['GET', 'POST'])
def select():

    return render_template('select.html', results=searched_movies)


@app.route('/add_selected', methods=['GET', 'POST'])
def add_selected():
    movie_to_add_title = request.args.get('title')
    movie_to_add_id = int(request.args.get('id'))
    for searched_movie in searched_movies:

        if searched_movie['id'] == movie_to_add_id:
            print(searched_movie)
            new_movie = Movie(
                title=searched_movie['title'],
                year=searched_movie['year'],
                description=searched_movie["description"],
                rating=searched_movie["rating"],
                img_url=f"https://image.tmdb.org/t/p/w500{searched_movie['img_url']}"
            )

            db.session.add(new_movie)
            db.session.commit()
    movie_selected = Movie.query.filter_by(title=f"{movie_to_add_title}").first()
    return redirect(url_for('edit', id=movie_selected.id))


if __name__ == '__main__':
    app.run(debug=True)
