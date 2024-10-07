#!/usr/bin/env python
from app.extensions import db

class Light(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    intensity = db.Column(db.Float, default=1.0)
    position = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    light_type_id = db.Column(db.Integer, db.ForeignKey('light_type.id'), nullable=False) # Foreign Key to LightType
    light_type = db.relationship('LightType', backref='lights') # Many-to-one relationship with lighttype

    def __repr__(self):
        return f'<Light {self.name}>'
