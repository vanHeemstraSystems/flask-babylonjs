#!/usr/bin/env python
from app.extensions import db

class FieldType(db.Model):
    __tablename__ = 'field_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<FieldType {self.name}>'
