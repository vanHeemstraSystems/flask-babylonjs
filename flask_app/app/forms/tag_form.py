#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class TagForm(FlaskForm):
   name = StringField('Field Name', validators=[DataRequired()])
   description = TextAreaField('Description')
   submit = SubmitField('Submit')