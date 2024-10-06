#!/usr/bin/env python
from app.extensions import db

class FieldType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<FieldType {self.name}>'