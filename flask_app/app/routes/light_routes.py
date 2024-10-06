#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.light import Light
from app.forms.light_form import LightForm
from app import db

light_bp = Blueprint('light', __name__)

@light_bp.route('/lights')
def list_lights():
   lights = Light.query.all()
   return render_template('lights.html', lights=lights)

@light_bp.route('/lights/new', methods=['GET', 'POST'])
def new_light():
   form = LightForm()
   if form.validate_on_submit():
       new_light = Light(
           name=form.name.data,
           light_type=form.light_type.data,
           intensity=form.intensity.data,
           position=form.position.data
       )
       db.session.add(new_light)
       db.session.commit()
       flash('Light created successfully!')
       return redirect(url_for('light.list_lights'))
   return render_template('new_light.html', form=form)

@light_bp.route('/lights/edit/<int:light_id>', methods=['GET', 'POST'])
def edit_light(light_id):
   light = Light.query.get_or_404(light_id)
   form = LightForm(obj=light)
   if form.validate_on_submit():
       light.name = form.name.data
       light.light_type = form.light_type.data
       light.intensity = form.intensity.data
       light.position = form.position.data
       db.session.commit()
       flash('Light updated successfully!')
       return redirect(url_for('light.list_lights'))
   return render_template('edit_light.html', form=form)