#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.player import Player
from app.extensions import db

player_bp = Blueprint('player', __name__)

@player_bp.route('/players')
def list_players():
   players = Player.query.all()
   return render_template('players.html', players=players)
