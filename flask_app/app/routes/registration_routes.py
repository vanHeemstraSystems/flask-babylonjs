#!/usr/bin/env python
from app.extensions import db, bcrypt
from app.decorators.registration_decorators import login_forbidden
from app.forms.registration_form import RegistrationForm
from app.models.user import User
from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import login_user

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/registration', methods=['GET', 'POST'])
@login_forbidden
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        pwd_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password_hash=pwd_hash, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('account created for ' + form.username.data, 'success')
        login_user(user, remember=True)
        return redirect(url_for('main.index'))
    return render_template('registration/registration.html', form=form)