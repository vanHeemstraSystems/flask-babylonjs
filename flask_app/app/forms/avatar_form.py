#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AvatarForm(FlaskForm):
    image_url = StringField('Avatar Image URL', validators=[DataRequired()])
    character_id = SelectField('Character', coerce=int, validators=[DataRequired()])  # Field for selecting Character
    submit = SubmitField('Submit')
