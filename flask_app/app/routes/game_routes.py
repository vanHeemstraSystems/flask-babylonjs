#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.game import Game
from app.forms.game_form import GameForm
from app.extensions import db

game_bp = Blueprint('game', __name__)

@game_bp.route('/games')
def list_games():
   games = Game.query.all()
   return render_template('games.html', games=games)

@game_bp.route('/join_game')
def join_game():
   return '<h1>Join Game</h1>'

@game_bp.route('/menu')
def menu():
   return '<h1>Game Menu Page</h1>'

@game_bp.route('/new_game')
def new_game():
   return '<h1>New Game Page</h1>'