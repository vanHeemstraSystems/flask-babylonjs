#!/usr/bin/env python
from app.extensions import bcrypt
from app.decorators.login_decorators import login_forbidden
from app.forms.login_form import LoginForm
from app.models.user import User
from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_user

login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
@login_forbidden
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('logged in')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        flash('error', 'danger')
    return render_template('login/login.html', form=form)