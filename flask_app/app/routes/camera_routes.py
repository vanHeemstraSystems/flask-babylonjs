#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.camera import Camera
from app.models.camera_type import CameraType
from app.forms.camera_form import CameraForm
from app.extensions import db

camera_bp = Blueprint('camera', __name__)

@camera_bp.route('/cameras')
def list_cameras():
   cameras = Camera.query.all()
   return render_template('cameras.html', cameras=cameras)

@camera_bp.route('/cameras/new', methods=['GET', 'POST'])
def new_camera():
   form = CameraForm()
   form.camera_type_id.choices = [(ct.id, ct.title) for ct in CameraType.query.all()]
   if form.validate_on_submit():
       new_camera = Camera(camera_type_id=form.camera_type_id.data, settings=form.settings.data)
       db.session.add(new_camera)
       db.session.commit()
       flash('Camera created successfully!')
       return redirect(url_for('camera.list_cameras'))
   return render_template('new_camera.html', form=form)

@camera_bp.route('/cameras/edit/<int:camera_id>', methods=['GET', 'POST'])
def edit_camera(camera_id):
   camera = Camera.query.get_or_404(camera_id)
   form = CameraForm(obj=camera)
   form.camera_type_id.choices = [(ct.id, ct.title) for ct in CameraType.query.all()]
   if form.validate_on_submit():
       camera.camera_type_id = form.camera_type_id.data
       camera.settings = form.settings.data
       db.session.commit()
       flash('Camera updated successfully!')
       return redirect(url_for('camera.list_cameras'))
   return render_template('edit_camera.html', form=form)

@camera_bp.route('/cameras/delete/<int:camera_id>', methods=['POST']) 
def delete_camera(camera_id):
    camera = Camera.query.get_or_404(camera_id)
    db.session.delete(camera)
    db.session.commit()
    flash('Camera deleted successfully!')
    return redirect(url_for('camera.list_cameras'))