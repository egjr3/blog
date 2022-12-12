from flask import Flask, render_template, request, redirect, url_for
from Models import db, Posts
import smtplib
import os

db_path = os.path.join(os.path.dirname(__file__), 'database/blog.db')
db_uri = 'sqlite:///{}'.format(db_path)

MY_EMAIL = "edgar.guerra.j@gmail.com"
MY_PASSWORD = "umowclhpclhvqpvx"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
db.init_app(app)


@app.route("/")
def home():
    all_posts = Posts.query.order_by(Posts.date)
    to_return = reversed([post.serialize() for post in all_posts])
    feedback = ''
    if not all_posts:
        feedback = 'Future Max, I promised myself I would keep updating the diary, come on, I know you can do this. :) <br><br> <a href="/publish">Click here to start Writing.</a>'
    return render_template('index.html', posts=to_return, message=feedback)


@app.route('/post/<id>')
def get_post(id):
    response_query = Posts.query.all()
    all_posts = [post.serialize() for post in response_query]
    post = {}
    for each in all_posts:
        if each['rowid'] == int(id):
            post = each

    paragraphs = post['content'].splitlines()
    return render_template("post.html", post=post, paragraphs=paragraphs)


@app.route("/publish")
def publish():
    return render_template('publish.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route('/form-entry', methods=['POST'])
def receive_data():
    name = request.form['name']
    sender_email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    feedback = ''
    try:
        #send_email(name, sender_email, phone, message)
        feedback = 'The email was sent successfully '
    except:
        feedback = 'There was an error sending the email'

    return render_template('contact.html', message = feedback)


def send_email(name, sender_email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {sender_email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=MY_EMAIL,
            msg=email_message
        )


@app.route('/publis-form', methods=['POST'])
def publishEntry():
    title = request.form['title']
    date = request.form['date']
    content = request.form['content']
    feedback = ''
    entry_rowid = publish_new_entry(title=title, date=date, content=content)

    try:
        feedback = f'Your <a href="/post/{entry_rowid}"><u>new entry</u><a> was published successfully.'
    except:
        feedback = 'There was an error publishing the new entry.'

    return render_template('publish.html', message = feedback)


def publish_new_entry(title, date, content):
    new_entry = f"""
    {{
    "body": "{content}",
    "title": "{title}",
    "date": "{date}"
    }}
    """
    new_post = Posts(title=title, date=date, content=content)
    db.session.add(new_post)
    db.session.commit()
    return new_post.rowid


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    to_delete_post = Posts.query.filter_by(rowid=post_id).first()
    db.session.delete(to_delete_post)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/edit/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    post = Posts.query.get(post_id)
    return render_template('edit.html', edit_post=post)

@app.route('/update_post/<int:post_id>', methods=["GET", "POST"])
def update_post(post_id):
    title = request.form['title']
    date = request.form['date']
    content = request.form['content']

    try:
        post = Posts.query.get(post_id)
        post.title = title
        post.date = date
        post.content = content
        db.session.commit()
    except:
        return render_template('edit.html', message='There was an error updating the entry.')

    return redirect(url_for('get_post', id=post_id))


if __name__ == '__main__':
    app.run(debug=True)