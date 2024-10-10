#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ShotForm(FlaskForm):
    title = StringField('Shot Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    shot_number = StringField('Shot Number', validators=[DataRequired()])
    camera_settings = StringField('Camera Settings (JSON)', validators=[DataRequired()])
    scene_id = SelectField('Scene', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')