#!/usr/bin/env python
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired

class LightForm(FlaskForm):
   name = StringField('Light Name', validators=[DataRequired()])
   light_type = SelectField('Light Type', choices=[('Point', 'Point'), ('Directional', 'Directional')], validators=[DataRequired()])
   intensity = FloatField('Intensity', default=1.0, validators=[DataRequired()])
   position = StringField('Position (JSON)', validators=[DataRequired()])
   submit = SubmitField('Submit')