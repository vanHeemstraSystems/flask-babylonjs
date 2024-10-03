#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint('scene3', __name__)

from app.scene3 import routes