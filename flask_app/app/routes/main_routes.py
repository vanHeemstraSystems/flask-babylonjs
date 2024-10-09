#!/usr/bin/env python
from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
