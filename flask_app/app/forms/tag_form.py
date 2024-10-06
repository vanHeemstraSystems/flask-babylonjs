#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TagForm(FlaskForm):
   title = StringField('Tag Title', validators=[DataRequired()])
   submit = SubmitField('Submit')