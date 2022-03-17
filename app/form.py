from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,IntegerField, SelectField,validators, TextAreaField
from wtforms.validators import InputRequired, DataRequired , Length

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    num_bed = IntegerField('No. of Rooms', validators=[InputRequired()])
    num_bath = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo ', validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    price = IntegerField('Price', validators=[InputRequired()])
    type = SelectField('Type', choices = [('House', 'House'),('Appartment','Appartment')])
    text = TextAreaField('Description',  validators=[DataRequired(),InputRequired(),Length(max=700)])
    