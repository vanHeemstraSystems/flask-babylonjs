#!/usr/bin/env python
from app.extensions import db

class Role(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(50), nullable=False, unique=True)

   def __repr__(self):
       return f'<Role {self.title}>'
