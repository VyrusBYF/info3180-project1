# pylint: disable=W0312
# pylint: disable=C0111
# pylint: disable=C0301

from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
	firstname = StringField('Firstname', validators=[InputRequired()])
	lastname = StringField('Lastname', validators=[InputRequired()])
	email = StringField('Email', validators=[InputRequired()])
	location = StringField('Location', validators=[InputRequired()])

	gender = SelectField('Gender', default=('Select Your Gender'), choices=[('Male', 'Male'), ('Female', 'Female')])

	bio = TextAreaField('Biograpghy')

	file = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
