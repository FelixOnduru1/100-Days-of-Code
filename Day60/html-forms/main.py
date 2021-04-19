from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def receive_data():
    username_entry = request.form['username']
    password_entry = request.form['password']
    return f"<h1>Name: {username_entry}, Password: {password_entry}</h1>"


if __name__ == "__main__":
    app.run(debug=True)