#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash 
from app.models.camera_type import CameraType 
from app.forms.camera_type_form import CameraTypeForm 
from app.extensions import db

camera_type_bp = Blueprint('camera_type', __name__)

@camera_type_bp.route('/camera_types')
def list_camera_types():
    camera_types = CameraType.query.all()
    return render_template('camera_types.html', camera_types=camera_types)

@camera_type_bp.route('/camera_types/new', methods=['GET', 'POST']) 
def new_camera_type():
    form = CameraTypeForm()
    if form.validate_on_submit():
        new_camera_type = CameraType(name=form.name.data, description=form.description.data)
        db.session.add(new_camera_type)
        db.session.commit()
        flash('Camera Type created successfully!')
        return redirect(url_for('camera_type.list_camera_types'))
    return render_template('new_camera_type.html', form=form)

@camera_type_bp.route('/camera_types/edit/<int:camera_type_id>', methods=['GET', 'POST']) 
def edit_camera_type(camera_type_id):
    camera_type = CameraType.query.get_or_404(camera_type_id)
    form = CameraTypeForm(obj=camera_type)
    if form.validate_on_submit():
        camera_type.name = form.name.data
        camera_type.description = form.description.data
        db.session.commit()
        flash('Camera Type updated successfully!')
        return redirect(url_for('camera_type.list_camera_types'))
    return render_template('edit_camera_type.html', form=form)

@camera_type_bp.route('/camera_types/delete/<int:camera_type_id>', methods=['POST']) 
def delete_camera_type(camera_type_id):
    camera_type = CameraType.query.get_or_404(camera_type_id)
    db.session.delete(camera_type)
    db.session.commit()
    flash('Camera Type deleted successfully!')
    return redirect(url_for('camera_type.list_camera_types'))