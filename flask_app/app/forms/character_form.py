#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CharacterForm(FlaskForm):
   name = StringField('Character Name', validators=[DataRequired()])
   description = TextAreaField('Description')
   submit = SubmitField('Submit')