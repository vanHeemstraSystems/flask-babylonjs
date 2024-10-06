#!/usr/bin/env python
from app.extensions import db

class Tag(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), nullable=False, unique=True)

   def __repr__(self):
       return f'<Tag {self.title}>'