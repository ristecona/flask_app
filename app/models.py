from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from app import db, login_manager

class Employee(UserMixin, db.Model):

	"""
	CREATE EMPLOYEE TABLE
	"""

	__tablename__ = 'employees'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(60), index = True, unique = True)
	username = db.Column(db.String(60), index = True, unique = True)
	firstname = db.Column(db.String(60), index = True)
	lastname = db.Column(db.String(60), index = True)
	password_hash = db.Column(db.String(128))
	department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	is_admin = db.Column(db.Boolean, default = False)

	@property
	def password(self):
		#PREVENT PASS FROM BEING ACCESSED
		raise AttributeError('Pass is not a readable atribute')

	@password.setter
	def password(self, password):
		#set pass to hashed pass
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		#check if actual pass matches hashed pass
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<Employee: {}>'.format(self.username)

#setup user_loader
@login_manager.user_loader
def load_user(user_id):
	return Employee.query.get(int(user_id))

class Department(db.Model):
	#CREATE DEPARTMENTS TABLE
	__tablename__ = 'departments'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(60), unique = True)
	description = db.Column(db.String(200))
	employees = db.relationship('Employee', backref='department',
		lazy='dynamic')

	def __repr__(self):
		return '<Department: {}>'.format(self.name)


class Role(db.Model):
	#CREATE A ROLE TABLE
	__tablename__ = 'roles'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(60))
	description = db.Column(db.String(200))
	employees = db.relationship('Employee', backref='role', lazy='dynamic')

	def __repr__(self):
		return '<Role: {}>'.format(self.name)
