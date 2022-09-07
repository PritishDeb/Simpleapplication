from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, length

class registration(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=2, max=20)])
    age = IntegerField('Age', validators=[DataRequired()])
    place = StringField('Place', validators=[DataRequired(), length(min=2, max=50)])
    submit = SubmitField('Submit')

