#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.profile import Profile
from app.forms.profile_form import ProfileForm
from app.extensions import db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/')
def list_profiles():
   profiles = Profile.query.all()
   return render_template('profiles.html', profiles=profiles)

@profile_bp.route('/new', methods=['GET', 'POST'])
def new_profile():
   form = ProfileForm()
   if form.validate_on_submit():
       new_profile = Profile(
           name=form.name.data,
           profile_type=form.profile_type.data,
           intensity=form.intensity.data,
           position=form.position.data
       )
       db.session.add(new_profile)
       db.session.commit()
       flash('Profile created successfully!')
       return redirect(url_for('profile.list_profiles'))
   return render_template('new_profile.html', form=form)

@profile_bp.route('/edit/<int:profile_id>', methods=['GET', 'POST'])
def edit_profile(profile_id):
   profile = Profile.query.get_or_404(profile_id)
   form = ProfileForm(obj=profile)
   if form.validate_on_submit():
       profile.name = form.name.data
       profile.profile_type = form.profile_type.data
       profile.intensity = form.intensity.data
       profile.position = form.position.data
       db.session.commit()
       flash('Profile updated successfully!')
       return redirect(url_for('profile.list_profiles'))
   return render_template('edit_profile.html', form=form)

@profile_bp.route('/view/<int:profile_id>', methods=['GET'])
def view_profile(profile_id):
   profile = Profile.query.get_or_404(profile_id)
   form = ProfileForm(obj=profile)
   return render_template('view_profile.html', form=form)