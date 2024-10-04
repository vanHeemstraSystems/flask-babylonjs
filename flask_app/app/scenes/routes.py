#!/usr/bin/env python
from flask import render_template
from app.scenes import bp
from app.extensions import db
from app.models.scene import Scene

@bp.route('/')
def index():
    scenes = Scene.query.all()
    return render_template('scenes/index.html', scenes=scenes)

@bp.route('/shots/')
def shots():
    return render_template('scenes/shots.html')