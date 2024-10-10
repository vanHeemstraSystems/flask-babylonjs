#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.story import Story
from app.extensions import db

story_bp = Blueprint('story', __name__)

@story_bp.route('/stories')
def list_stories():
   stories = Story.query.all()
   return render_template('stories.html', stories=stories)
