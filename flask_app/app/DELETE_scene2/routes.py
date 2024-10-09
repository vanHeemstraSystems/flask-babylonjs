#!/usr/bin/env python
from flask import render_template
from app.scene2 import bp
from app.extensions import db
from app.models.scene2 import Scene2

@bp.route('/')
def index():
    return render_template('scene2/index.html')