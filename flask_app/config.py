#!/usr/bin/env python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False