#!/usr/bin/env python
from app.extensions import db

class CharacterType(db.Model):
    __tablename__ = 'character_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character = db.relationship('Character', backref='character_types') # Relationship with Character
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<CharacterType Character ID: {self.character_id}>'