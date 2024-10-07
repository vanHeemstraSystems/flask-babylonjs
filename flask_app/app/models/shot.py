#!/usr/bin/env python
from app.extensions import db

class Shot(db.Model):
    __tablename__ = 'shot'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    camera_settings = db.Column(db.String(200), nullable=False)  # JSON settings for the camera
    scene_id = db.Column(db.Integer, db.ForeignKey('scene.id'), nullable=False)  # Foreign Key to Scene
    shot_type_id = db.Column(db.Integer, db.ForeignKey('shot_type.id'), nullable=False) # Foreign Key to ShotType
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    scene = db.relationship('Scene', backref='shots')  # One-to-many relationship with Scene
    shot_type = db.relationship('ShotType', backref='shots') # Many-to-one relationship with ShotType

    def __repr__(self):
        return f'<Shot {self.title}>'
