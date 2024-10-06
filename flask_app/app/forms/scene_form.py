#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SceneForm(FlaskForm):
   title = StringField('Scene Title', validators=[DataRequired()])
   scene_number = StringField('Scene Number', validators=[DataRequired()])
   submit = SubmitField('Submit')