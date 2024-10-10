#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user_role import UserRole
from app.forms.user_role_form import UserRoleForm
from app.extensions import db

user_role_bp = Blueprint('user_role', __name__)
