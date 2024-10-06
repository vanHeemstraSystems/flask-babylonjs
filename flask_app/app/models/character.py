#!/usr/bin/env python
from app.extensions import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Character {self.name}>'
