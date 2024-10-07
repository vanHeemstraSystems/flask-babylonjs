#!/usr/bin/env python
from app.extensions import db

class Light(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    light_type = db.Column(db.String(50), nullable=False)
    intensity = db.Column(db.Float, default=1.0)
    position = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Light {self.name}, Light_Type: {self.light_type}, Intensity: {self.intensity}>'
