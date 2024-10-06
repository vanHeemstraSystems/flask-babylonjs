#!/usr/bin/env python
from app.extensions import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    release_date = db.Column(db.Date, nullable=True)
    genre = db.Column(db.String(50), nullable=True)

    users = db.relationship('User', secondary='user_game', backref='games')

    def __repr__(self):
        return f'<Game {self.title}>'