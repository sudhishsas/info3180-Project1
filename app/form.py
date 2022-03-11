from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,IntegerField, validators

class PropertyForm(FlaskForm):
    title = StringField('Username', validators=[InputRequired()])
    num_bed = StringField('Username', validators=[InputRequired()])
    