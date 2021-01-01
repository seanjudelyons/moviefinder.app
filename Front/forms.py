from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length



class Ask(FlaskForm):
    query = StringField('Search by Movie Plot', validators=[DataRequired(), Length(min=2, max=480)])
    submit = SubmitField('Search')
