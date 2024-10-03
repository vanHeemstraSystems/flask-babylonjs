#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint('scene1', __name__)

from app.scene1 import routes