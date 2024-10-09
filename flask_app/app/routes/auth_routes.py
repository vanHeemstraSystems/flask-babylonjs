from app.extensions import db, bcrypt
from app.auth.decorators import login_forbidden
from app.auth.forms import RegistrationForm, LoginForm
from app.models.user import User
from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)