#!/usr/bin/env python
from flask import render_template
from app.scene3 import bp
from app.extensions import db
from app.models.scene3 import Scene1

@bp.route('/')
def index():
    return render_template('scene3/index.html')