#!/usr/bin/env python
from app.extensions import db

class Avatar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(200), nullable=False)  # URL to the avatar image
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)  # Foreign Key to Character

    character = db.relationship('Character', backref='avatar', uselist=False)  # One-to-one relationship with Character

    def __repr__(self):
        return f'<Avatar Character ID: {self.character_id}, Image URL: {self.image_url}>'
