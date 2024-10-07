#!/usr/bin/env python
from app.extensions import db

class Camera(db.Model):
   __tablename__ = 'camera'
   id = db.Column(db.Integer, primary_key=True)
   camera_type_id = db.Column(db.Integer, db.ForeignKey('camera_type.id'), nullable=False)
   settings = db.Column(db.String(200), nullable=False)
   created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
   camera_type = db.relationship('CameraType', backref='cameras')

   def __repr__(self):
     return f'<Camera {self.id}, Camera_Type: {self.camera_type}>'
