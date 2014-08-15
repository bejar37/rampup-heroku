from flask import Flask, render_template, url_for, redirect, request
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
app.debug = True
db = SQLAlchemy(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def getUserForm():
    return render_template("hello.html", users=User.query.all())

@app.route("/user/create", methods=["POST"])
def createUser():
    print request.form
    print request.method
    uname = request.form["username"]
    email = request.form["email"]
    print email, uname
    db.session.add(User(uname, email))
    db.session.commit()
    print "HELLO!"
    return redirect(url_for("getUserForm"))


if __name__ == "__main__":
    app.run()
