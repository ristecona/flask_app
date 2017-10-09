from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')

def homepage():
	#render homepage
	return render_template('home/index.html', title = 'WELCOME')

@home.route('/dashboard')
@login_required

def dashboard():
	#render dashboard template
	return render_template('/home/dashboard.html', title='Dashboard')