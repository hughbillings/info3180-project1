from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email


class UploadForm(FlaskForm):
    fname = StringField('First Name',validators=[DataRequired()])
    lname = StringField('Last Name',validators=[DataRequired()])
    gender = SelectField('Gender',choices=[('male','Male'),('female','Female')])
    email = StringField('Email', validators=[DataRequired(),Email()])
    location = StringField('Location',validators=[DataRequired()])
    biography = TextAreaField('Biography',validators=[DataRequired()])
    file = FileField('Profile Image',validators=[FileRequired(),FileAllowed(['jpg','png'])])