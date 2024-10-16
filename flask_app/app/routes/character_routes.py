#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.character import Character
from app.forms.character_form import CharacterForm
from app.extensions import db

character_bp = Blueprint('character', __name__)

@character_bp.route('/')
def list_characters():
   characters = Character.query.all()
   return render_template('characters.html', characters=characters)