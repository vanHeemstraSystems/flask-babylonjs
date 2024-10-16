#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ProfileForm(FlaskForm):
    profilename = StringField('Profilename')
    submit = SubmitField('Submit')