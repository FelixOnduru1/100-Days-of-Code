from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(email=request.form['email']):
            flash("You have already signed up with that email, log in instead.")
            return redirect(url_for("login"))
        else:
            new_user = User(
                name=request.form['name'],
                email=request.form['email'],
                password=generate_password_hash(password=request.form['password'], method='pbkdf2:sha256', salt_length=8),
            )
            db.session.add(new_user)
            db.session.commit()

            return render_template('secrets.html', name=new_user.name)
    else:
        return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user:
            entered_password = request.form['password']
            if check_password_hash(pwhash=user.password, password=entered_password):
                login_user(user)
                return render_template("secrets.html", name=user.name, logged_in=current_user.is_authenticated)
            else:
                flash("The password you entered is incorrect. Please try again.")
                return redirect(url_for('login'))
        else:
            flash("The email does not exist. Please try again.")
            return redirect(url_for('login'))

    else:
        return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
def secrets():
    return render_template("secrets.html", logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("index.html")


@app.route('/download')
@login_required
def download():

    return send_from_directory(directory="static/files", filename='cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
