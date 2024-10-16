#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.board import Board
from app.extensions import db

board_bp = Blueprint('board', __name__)

@board_bp.route('/')
def list_boards():
   boards = Board.query.all()
   return render_template('boards.html', boards=boards)