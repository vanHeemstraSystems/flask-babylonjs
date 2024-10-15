#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.avatar import Avatar
from app.models.character import Character  # Import Character to populate the select field
from app.extensions import db
from app.forms.avatar_form import AvatarForm

avatar_bp = Blueprint('avatar', __name__)

@avatar_bp.route('/avatars')
def list_avatars():
    avatars = Avatar.query.all()
    return render_template('avatars.html', avatars=avatars)

@avatar_bp.route('/avatars/new', methods=['GET', 'POST'])
def new_avatar():
    form = AvatarForm()
    form.character_id.choices = [(character.id, character.name) for character in Character.query.all()]  # Populate Character choices
    if form.validate_on_submit():
        new_avatar = Avatar(image_url=form.image_url.data, character_id=form.character_id.data)  # Set Character ID
        db.session.add(new_avatar)
        db.session.commit()
        flash('Avatar created successfully!')
        return redirect(url_for('avatar.list_avatars'))
    return render_template('new_avatar.html', form=form)

@avatar_bp.route('/avatars/edit/<int:avatar_id>', methods=['GET', 'POST'])
def edit_avatar(avatar_id):
    avatar = Avatar.query.get_or_404(avatar_id)
    form = AvatarForm(obj=avatar)
    form.character_id.choices = [(character.id, character.name) for character in Character.query.all()]  # Populate Character choices
    if form.validate_on_submit():
        avatar.image_url = form.image_url.data
        avatar.character_id = form.character_id.data  # Update Character ID
        db.session.commit()
        flash('Avatar updated successfully!')
        return redirect(url_for('avatar.list_avatars'))
    return render_template('edit_avatar.html', form=form)

@avatar_bp.route('/avatars/delete/<int:avatar_id>', methods=['POST'])
def delete_avatar(avatar_id):
    avatar = Avatar.query.get_or_404(avatar_id)
    db.session.delete(avatar)
    db.session.commit()
    flash('Avatar deleted successfully!')
    return redirect(url_for('avatar.list_avatars'))
