from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import sqlite3


app = Flask(__name__)



# Creates a new database called books-collection
# db = sqlite3.connect("books-collection.db")

# Creates a cursor that modifies the database
# cursor = db.cursor()
# This Code creates the database
# cursor.execute("CREATE TABLE books"
#                " (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,"
#                " author varchar(250) NOT NULL,"
#                " rating FLOAT NOT NULL)")

# Adding a new row and committing
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create Table


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    review = db.Column(db.Float, nullable=False)

# Allows each book to be identified by its title when printed
    def __repr__(self):
        return f"<Book {self.title}>"


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Books).all()

    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Books(title=request.form['title'],
                         author=request.form['author'],
                         review=float(request.form['rating'])
                         )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        return render_template('add.html')


@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    book_to_update = Books.query.get(book_id)
    if request.method == 'POST':
        book_to_update.review = request.form['rating']
        db.session.commit()

        return redirect(url_for('home'))
    else:
        return render_template('edit.html', book=book_to_update)


@app.route('/delete')
def delete():
    book_id = request.args.get('book_id')
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
