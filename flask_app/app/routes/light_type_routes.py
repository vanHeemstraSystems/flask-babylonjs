#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash 
from app.models.light_type import LightType 
from app.forms.light_type_form import LightTypeForm 
from app.extensions import db

light_type_bp = Blueprint('light_type', __name__)

@light_type_bp.route('/')
def list_light_types():
    light_types = LightType.query.all()
    return render_template('light_types.html', light_types=light_types)

@light_type_bp.route('/new', methods=['GET', 'POST']) 
def new_light_type():
    form = LightTypeForm()
    if form.validate_on_submit():
        new_light_type = LightType(name=form.name.data, description=form.description.data)
        db.session.add(new_light_type)
        db.session.commit()
        flash('Light Type created successfully!')
        return redirect(url_for('light_type.list_light_types'))
    return render_template('new_light_type.html', form=form)

@light_type_bp.route('/edit/<int:light_type_id>', methods=['GET', 'POST']) 
def edit_light_type(light_type_id):
    light_type = LightType.query.get_or_404(light_type_id)
    form = LightTypeForm(obj=light_type)
    if form.validate_on_submit():
        light_type.name = form.name.data
        light_type.description = form.description.data
        db.session.commit()
        flash('Light Type updated successfully!')
        return redirect(url_for('light_type.list_light_types'))
    return render_template('edit_light_type.html', form=form)

@light_type_bp.route('/delete/<int:light_type_id>', methods=['POST']) 
def delete_light_type(light_type_id):
    light_type = LightType.query.get_or_404(light_type_id)
    db.session.delete(light_type)
    db.session.commit()
    flash('Light Type deleted successfully!')
    return redirect(url_for('light_type.list_light_types'))
