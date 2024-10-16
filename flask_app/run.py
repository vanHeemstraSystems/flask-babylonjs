#!/usr/bin/env python
import os
from app import create_app
from app.extensions import db, socketio

app = create_app()

if __name__ == "__main__":
    print("Starting socketio") # Use $ python3 run.py
    socketio.run(app)