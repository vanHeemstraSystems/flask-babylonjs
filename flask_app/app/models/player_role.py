#!/usr/bin/env python
from app.extensions import db

class PlayerRole(db.Model):
    __tablename__ = 'player_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)
    player_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    player = db.relationship('Player', backref='player_roles') # Relationship with Player

    def __repr__(self):
        return f'<PlayerRole Player ID: {self.player_id}>'
