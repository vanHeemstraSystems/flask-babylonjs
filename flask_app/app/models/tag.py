#!/usr/bin/env python
from app.extensions import db

class Tag(db.Model):
   __tablename__ = 'tag'
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), nullable=False, unique=True)
   created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

   def __repr__(self):
       return f'<Tag {self.title}>'
