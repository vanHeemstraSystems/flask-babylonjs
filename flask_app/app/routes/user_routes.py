#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user import User
from app.forms.user_form import UserForm
from app.extensions import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def list_users():
   users = User.query.all()
   return render_template('users.html', users=users)