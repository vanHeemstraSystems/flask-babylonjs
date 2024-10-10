#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired

class GameForm(FlaskForm):
    title = StringField('Game Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    release_date = DateField('Release Date', format='%Y-%m-%d', validators=[DataRequired()])
    genre = StringField('Genre')
    board_id = SelectField('Board', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')