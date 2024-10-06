#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CameraForm(FlaskForm):
   camera_type_id = SelectField('Camera Type', coerce=int, validators=[DataRequired()])
   settings = StringField('Settings', validators=[DataRequired()])
   submit = SubmitField('Submit')