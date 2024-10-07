#!/usr/bin/env python
from app.extensions import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    score = db.Column(db.Integer, default=0)  # Example field to track player score
    level = db.Column(db.Integer, default=1)  # Example field to track player level
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    user = db.relationship('User', backref='players')  # Relationship with User
    character = db.relationship('Character', backref='players')  # Relationship with Character

    def __repr__(self):
        return f'<Player User ID: {self.user_id}, Character ID: {self.character_id}>'
