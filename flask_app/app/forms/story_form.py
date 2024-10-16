#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired

class StoryForm(FlaskForm):
    title = StringField('Story Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    release_date = DateField('Release Date', format='%Y-%m-%d', validators=[DataRequired()])
    genre = StringField('Genre')
    content = TextAreaField('Content')
    submit = SubmitField('Submit')