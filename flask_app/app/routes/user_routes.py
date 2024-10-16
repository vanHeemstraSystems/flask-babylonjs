#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import model_user, model_profile
from app.forms.user_form import UserForm
from app.extensions import db, bcrypt

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def list_users():
   users = model_user.query.all()
   return render_template('users.html', users=users)
 
@user_bp.route('/new', methods=['GET', 'POST'])
def new_user():
   form = UserForm()
   if form.validate_on_submit():
       pwd_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
       new_user = model_user(username=form.username.data, email=form.email.data, password_hash=pwd_hash)
       # Create a profile for a user
       new_profile = model_profile(profilename=form.username.data, user=new_user) # Set profilename to username
       db.session.add(new_user)
       db.session.add(new_profile)
       db.session.commit()
       flash('User and Profile created successfully!')
       return redirect(url_for('prop.list_users'))
   return render_template('new_user.html', form=form)

@user_bp.route('/edit/<int:prop_id>', methods=['GET', 'POST'])
def edit_user(user_id):
   user = model_user.query.get_or_404(user_id)
   form = UserForm(obj=user)
   if form.validate_on_submit():
       user.name = form.name.data
       user.model_url = form.model_url.data
       db.session.commit()
       flash('User updated successfully!')
       return redirect(url_for('user.list_users'))
   return render_template('edit_user.html', form=form)