#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint('scene2', __name__)

from app.scene2 import routes