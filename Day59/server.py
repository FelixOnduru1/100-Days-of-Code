from flask import Flask, render_template, request
import requests
import smtplib
import os

my_email = "pythonsmtp404@gmail.com"

password = os.environ["EMAIL_PASSWORD"]

blog_posts = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965").json()


def send_mail(email_message):
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:NEW MESSAGE FROM THE ONDURU'S BLOG\n\n{email_message}".encode('utf-8')
                            )


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html", posts=blog_posts)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        data = request.form

        final_message = f'Name: {data["username"]}\n' \
                        f'Email: {data["email"]}\n' \
                        f'Phone: {data["phone"]}\n' \
                        f'Message: {data["message"]}'
        send_mail(final_message)
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:number>')
def post_page(number):
    requested_post = None
    for blog_post in blog_posts:
        if blog_post["id"] == number:
            requested_post = blog_post
            print(requested_post)

    return render_template("post.html", post=requested_post)





if __name__ == "__main__":
    app.run(debug=True)
