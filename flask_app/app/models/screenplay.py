#!/usr/bin/env python
from app.extensions import db

class Screenplay(db.Model):
    __tablename__ = 'screenplay'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    release_date = db.Column(db.Date, nullable=True)
    genre = db.Column(db.String(50), nullable=True)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'), nullable=False) # Foreign Key to Story
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    story = db.relationship('Story', backref='screenplays') # One-to-many relationship with Story
    
    def __repr__(self):
        return f'<Screenplay {self.title}>'
