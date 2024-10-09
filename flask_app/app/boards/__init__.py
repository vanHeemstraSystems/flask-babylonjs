#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint('boards', __name__)

from app.routes.board_routes import routes
