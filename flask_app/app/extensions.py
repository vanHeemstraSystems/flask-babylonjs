#!/usr/bin/env python
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO()
