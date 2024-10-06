#!/usr/bin/env python
from app.extensions import db

class Camera(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   camera_type_id = db.Column(db.Integer, db.ForeignKey('camera_type.id'), nullable=False)
   settings = db.Column(db.String(200), nullable=False)

   camera_type = db.relationship('CameraType', backref='cameras')

   def __repr__(self):
     return f'<Camera {self.id}, Camera_Type: {self.camera_type}>'