#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.field import Field
from app.forms.field_form import FieldForm
from app.extensions import db

field_bp = Blueprint('field', __name__)

@field_bp.route('/fields')
def list_fields():
   fields = Field.query.all()
   return render_template('fields.html', fields=fields)