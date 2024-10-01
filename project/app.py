from flask import Flask
from pathlib import Path
import sqlite3
from flask import Flask, g, render_template, request, session, flash, redirect, url_for, abort, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()
# create and initialize a new Flask app
app = Flask(__name__)

# load the config
basedir = Path(__file__).resolve().parent
app.config["DATABASE"] = os.getenv("DATABASE")
app.config["USERNAME"] = os.getenv("USERNAME")
app.config["PASSWORD"] = os.getenv("PASSWORD")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{Path(basedir).joinpath(app.config["DATABASE"])}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# connect to database
db = SQLAlchemy(app)
from project import models
with app.app_context():
    db.create_all()
    db.session.commit()

@app.route('/')
def index():
    """Searches the database for entries, then displays them."""
    entries = db.session.query(models.Post).order_by(models.Post.id.desc())
    return render_template('index.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    """Adds new post to the database."""
    if not session.get('logged_in'):
        abort(401)
    new_entry = models.Post(request.form['title'], request.form['text'])
    db.session.add(new_entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login/authentication/session management."""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    """User logout/authentication/session management."""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))


@app.route('/delete/<int:post_id>', methods=['GET'])
def delete_entry(post_id):
    """Deletes post from database."""
    result = {'status': 0, 'message': 'Error'}
    try:
        db.session.query(models.Post).filter_by(id=post_id).delete()
        db.session.commit()
        result = {'status': 1, 'message': "Post Deleted"}
        flash('The entry was deleted.')
    except Exception as e:
        result = {'status': 0, 'message': repr(e)}
    return jsonify(result)


if __name__ == "__main__":
    print(app.config["DATABASE"], app.config["USERNAME"], app.config["PASSWORD"])
    app.run()