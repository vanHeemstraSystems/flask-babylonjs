#!/usr/bin/env python
from app.extensions import db

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    release_date = db.Column(db.Date, nullable=True)
    genre = db.Column(db.String(50), nullable=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False) # Foreign Key to Board
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False) # Foreign Key to Story
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    board = db.relationship('Board', backref='game', uselist=False) # One-to-one relationship with Board
    story = db.relationship('Story', backref='games') # One-to-many relationship with Story
    # users = db.relationship('User', secondary='user_game', backref='games') # REMOVE

    def __repr__(self):
        return f'<Game {self.title}>'
