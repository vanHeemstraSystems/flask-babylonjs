#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class PlayerForm(FlaskForm):
    user_id = SelectField('User', coerce=int, validators=[DataRequired()])
    character_id = SelectField('Character', coerce=int, validators=[DataRequired()])
    score = IntegerField('Score', default=0)
    level = IntegerField('Level', default=1)
    submit = SubmitField('Submit')