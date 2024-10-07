#!/usr/bin/env python
from app.extensions import db

class CharacterRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<CharacterRole {self.name}>'
