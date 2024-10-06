#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PropForm(FlaskForm):
   name = StringField('Prop Name', validators=[DataRequired()])
   model_url = StringField('Model URL', validators=[DataRequired()])
   submit = SubmitField('Submit')