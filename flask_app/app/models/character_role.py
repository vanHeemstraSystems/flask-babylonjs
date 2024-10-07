#!/usr/bin/env python
from app.extensions import db

class CharacterRole(db.Model):
    __tablename__ = 'character_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character = db.relationship('Character', backref='character_roles') # Relationship with Character

    def __repr__(self):
        return f'<CharacterRole Character ID: {self.character_id}>'
