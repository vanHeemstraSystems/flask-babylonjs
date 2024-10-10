#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

class UserCharacterForm(FlaskForm):
    characters = SelectMultipleField('Characters', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')