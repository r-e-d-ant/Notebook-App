
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from notebook_app.models import User

# ====================================================== NOTES PART ============================= 
class UpdateNoteForm(FlaskForm):
	subject = StringField('Subject', validators=[DataRequired()])
	notes = TextAreaField('Notes', validators=[DataRequired()])

	updateNoteBtn = SubmitField('Update')

class NewSubjectForm(FlaskForm):
	subjects_name = StringField('Add new subject here', validators=[DataRequired()])
	
	submitSubjectUpdateBtn = SubmitField('SAVE')

# ====================================================== ••••••••••• ============================= 

# ====================================================== USER PART ============================= 
# ========== REGISTERING FORM ==============
class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_pasword = PasswordField('Confirm password', validators=[DataRequired()])

	RegisterBtn = SubmitField('Sign Up')

	# Validations

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one')

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('That email is taken. Please choose a different one')

# ========== LOGIN FORM ==============

class LoginForm(FlaskForm):
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])

	loginBtn = SubmitField('Log In')


# ========== UPDATE ACCOUNT FORM ==============

class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField("Email", validators=[DataRequired(), Email()])

	updateAccBtn = SubmitField('Update')

	# Validations

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one')

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('That email is taken. Please choose a different one')

# ====================================================== ••••••••• ============================= 


