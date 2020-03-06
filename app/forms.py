# pylint: disable=W0312
# pylint: disable=C0111

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired, FileRequired, FileAllowed

class UserForm(FlaskForm):
	firstname = StringField('Firstname', validators=[InputRequired()])
	lastname = StringField('Lastname', validators=[InputRequired()])
	email = StringField('Email', validators=[InputRequired()])
	location = StringField('Email', validators=[InputRequired()])

	gender = SelectField('Gender', choices=['Male', 'Female'])

	bio = TextAreaField('Biograpghy')

	file = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
