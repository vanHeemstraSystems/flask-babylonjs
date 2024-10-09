#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash 
from app.models.field_type import FieldType 
from app.forms.field_type_form import FieldTypeForm 
from app.extensions import db

field_type_bp = Blueprint('field_type', __name__)

@field_type_bp.route('/field_types')
def list_field_types():
    field_types = FieldType.query.all()
    return render_template('field_types.html', field_types=field_types)

@field_type_bp.route('/field_types/new', methods=['GET', 'POST']) 
def new_field_type():
    form = FieldTypeForm()
    if form.validate_on_submit():
        new_field_type = FieldType(name=form.name.data, description=form.description.data)
        db.session.add(new_field_type)
        db.session.commit()
        flash('Field Type created successfully!')
        return redirect(url_for('field_type.list_field_types'))
    return render_template('new_field_type.html', form=form)

@field_type_bp.route('/field_types/edit/<int:field_type_id>', methods=['GET', 'POST']) 
def edit_field_type(field_type_id):
    field_type = FieldType.query.get_or_404(field_type_id)
    form = FieldTypeForm(obj=field_type)
    if form.validate_on_submit():
        field_type.name = form.name.data
        field_type.description = form.description.data
        db.session.commit()
        flash('Field Type updated successfully!')
        return redirect(url_for('field_type.list_field_types'))
    return render_template('edit_field_type.html', form=form)

@field_type_bp.route('/field_types/delete/<int:field_type_id>', methods=['POST']) 
def delete_field_type(field_type_id):
    field_type = FieldType.query.get_or_404(field_type_id)
    db.session.delete(field_type)
    db.session.commit()
    flash('Field Type deleted successfully!')
    return redirect(url_for('field_type.list_field_types'))