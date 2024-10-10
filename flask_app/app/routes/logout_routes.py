#!/usr/bin/env python
from flask import Blueprint, redirect, url_for
from flask_login import logout_user, login_required

logout = Blueprint('logout', __name__)

@logout.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
