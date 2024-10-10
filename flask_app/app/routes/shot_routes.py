#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.shot import Shot
from app.extensions import db

shot_bp = Blueprint('shot', __name__)

@shot_bp.route('/shots')
def list_shots():
   shots = Shot.query.all()
   return render_template('shots.html', shots=shots)
