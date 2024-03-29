import requests
from flask import Flask, render_template
BLOG_URL = "https://api.npoint.io/5abcca6f4e39b4955965"
blog_posts = requests.get(url=BLOG_URL).json()


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html", posts=blog_posts)


@app.route('/post/<int:number>')
def post_page(number):
    requested_post = None
    for blog_post in blog_posts:
        if blog_post["id"] == number:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
