#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.screenplay import Screenplay
from app.extensions import db

screenplay_bp = Blueprint('screenplay', __name__)

@screenplay_bp.route('/')
def list_screenplays():
   screenplays = Screenplay.query.all()
   return render_template('screenplays.html', screenplays=screenplays)
