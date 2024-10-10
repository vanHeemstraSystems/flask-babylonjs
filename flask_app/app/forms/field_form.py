#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class FieldForm(FlaskForm):
    name = StringField('Field Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    field_type_id = SelectField('Field Type', coerce=int, validators=[DataRequired()])
    board_id = SelectField('Board', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')