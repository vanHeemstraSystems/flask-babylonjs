#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint('scenes', __name__)

from app.scenes import routes