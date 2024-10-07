#!/usr/bin/env python
from app.extensions import db

# class Scene(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150))
#     content = db.Column(db.Text)

#     def __repr__(self):
#         return f'<Scene "{self.title}">'

class Scene(db.Model):
   __tablename__ = 'scene'
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), nullable=False)
   scene_number = db.Column(db.String(50), nullable=True)
   characters = db.relationship('Character', secondary='character_scene', backref='scenes', lazy='dynamic')
   props = db.relationship('Prop', secondary='prop_scene', backref='scenes', lazy='dynamic')
   lights = db.relationship('Light', secondary='light_scene', backref='scenes', lazy='dynamic')
   tags = db.relationship('Tag', secondary='scene_tag', backref='scenes', lazy='dynamic')

   def __repr__(self):
       return f'<Scene {self.title}, Number: {self.scene_number}>'
