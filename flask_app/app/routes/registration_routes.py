#!/usr/bin/env python
from app.extensions import db, bcrypt
#from app.decorators.login_decorators import login_forbidden
#from app.forms.login_form import LoginForm
from app.forms.registration_form import RegistrationForm
from app.models.user import User
from flask import Blueprint, redirect, url_for, render_template, flash, request
#from flask_login import login_user, logout_user, login_required

registration = Blueprint('registration', __name__)