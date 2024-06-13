from flask import Blueprint, render_template

bp = Blueprint('garage_proj', __name__)

@bp.route('/')
def home():
    return render_template('pages/home.html')
               
@bp.route('/daily')
def daily():
    return render_template('pages/daily.html')

@bp.route('/monthly')
def monthly():
    return render_template('pages/monthly.html')

@bp.route('/about')
def about():
    return render_template('pages/about.html')