#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash 
from app.models.shot_type import ShotType 
from app.forms.shot_type_form import ShotTypeForm 
from app.extensions import db

shot_type_bp = Blueprint('shot_type', __name__)

@shot_type_bp.route('/shot_types')
def list_shot_types():
    shot_types = ShotType.query.all()
    return render_template('shot_types.html', shot_types=shot_types)

@shot_type_bp.route('/shot_types/new', methods=['GET', 'POST']) def new_shot_type():
    form = ShotTypeForm()
    if form.validate_on_submit():
        new_shot_type = ShotType(name=form.name.data, description=form.description.data)
        db.session.add(new_shot_type)
        db.session.commit()
        flash('Shot Type created successfully!')
        return redirect(url_for('shot_type.list_shot_types'))
    return render_template('new_shot_type.html', form=form)

@shot_type_bp.route('/shot_types/edit/<int:shot_type_id>', methods=['GET', 'POST']) def edit_shot_type(shot_type_id):
    shot_type = ShotType.query.get_or_404(shot_type_id)
    form = ShotTypeForm(obj=shot_type)
    if form.validate_on_submit():
        shot_type.name = form.name.data
        shot_type.description = form.description.data
        db.session.commit()
        flash('Shot Type updated successfully!')
        return redirect(url_for('shot_type.list_shot_types'))
    return render_template('edit_shot_type.html', form=form)

@shot_type_bp.route('/shot_types/delete/<int:shot_type_id>', methods=['POST']) def delete_shot_type(shot_type_id):
    shot_type = ShotType.query.get_or_404(shot_type_id)
    db.session.delete(shot_type)
    db.session.commit()
    flash('Shot Type deleted successfully!')
    return redirect(url_for('shot_type.list_shot_types'))

