from flask import Blueprint, render_template

# tells flask that views.py containing a bunch of url or routes
views= Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')