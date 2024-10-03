#!/usr/bin/env python
from flask import render_template
from app.scene1 import bp
from app.extensions import db
from app.models.scene1 import Scene1

@bp.route('/')
def index():
    return render_template('scene1/index.html')