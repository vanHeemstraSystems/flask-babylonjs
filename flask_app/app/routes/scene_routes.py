#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.scene import Scene
from app.forms.scene_form import SceneForm
from app.extensions import db

scene_bp = Blueprint('scene', __name__)

@scene_bp.route('/')
def list_scenes():
   scenes = Scene.query.all()
   return render_template('scenes.html', scenes=scenes)

@scene_bp.route('/new', methods=['GET', 'POST'])
def new_scene():
   form = SceneForm()
   if form.validate_on_submit():
       new_scene = Scene(title=form.title.data, scene_number=form.scene_number.data)
       db.session.add(new_scene)
       db.session.commit()
       flash('Scene created successfully!')
       return redirect(url_for('scene.list_scenes'))
   return render_template('new_scene.html', form=form)

@scene_bp.route('/edit/<int:scene_id>', methods=['GET', 'POST'])
def edit_scene(scene_id):
   scene = Scene.query.get_or_404(scene_id)
   form = SceneForm(obj=scene)
   if form.validate_on_submit():
       scene.title = form.title.data
       scene.scene_number = form.scene_number.data
       db.session.commit()
       flash('Scene updated successfully!')
       return redirect(url_for('scene.list_scenes'))
   return render_template('edit_scene.html', form=form)