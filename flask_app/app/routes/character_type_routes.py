#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash 
from app.models.character_type import CharacterType 
from app.forms.character_type_form import CharacterTypeForm 
from app.extensions import db

character_type_bp = Blueprint('character_type', __name__)

@character_type_bp.route('/character_types')
def list_character_types():
    character_types = CharacterType.query.all()
    return render_template('character_types.html', character_types=character_types)

@character_type_bp.route('/character_types/new', methods=['GET', 'POST']) 
def new_character_type():
    form = CharacterTypeForm()
    if form.validate_on_submit():
        new_character_type = CharacterType(name=form.name.data, description=form.description.data)
        db.session.add(new_character_type)
        db.session.commit()
        flash('Character Type created successfully!')
        return redirect(url_for('character_type.list_character_types'))
    return render_template('new_character_type.html', form=form)

@character_type_bp.route('/character_types/edit/<int:character_type_id>', methods=['GET', 'POST']) 
def edit_character_type(character_type_id):
    character_type = CharacterType.query.get_or_404(character_type_id)
    form = CharacterTypeForm(obj=character_type)
    if form.validate_on_submit():
        character_type.name = form.name.data
        character_type.description = form.description.data
        db.session.commit()
        flash('Character Type updated successfully!')
        return redirect(url_for('character_type.list_character_types'))
    return render_template('edit_character_type.html', form=form)

@character_type_bp.route('/character_types/delete/<int:character_type_id>', methods=['POST']) 
def delete_character_type(character_type_id):
    character_type = CharacterType.query.get_or_404(character_type_id)
    db.session.delete(character_type)
    db.session.commit()
    flash('Character Type deleted successfully!')
    return redirect(url_for('character_type.list_character_types'))