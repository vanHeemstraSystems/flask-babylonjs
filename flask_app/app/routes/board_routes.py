#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.board import Board
# from app.models.camera_type import CameraType
# from app.forms.camera_form import CameraForm
from app.extensions import db

board_bp = Blueprint('board', __name__)

# routes