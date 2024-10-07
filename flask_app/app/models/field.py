#!/usr/bin/env python
from app.extensions import db

class Field(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    field_type_id = db.Column(db.Integer, db.ForeignKey('field_type.id'), nullable=False)  # Foreign Key to FieldType
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)  # Foreign Key to Board
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    field_type = db.relationship('FieldType', backref='fields')  # Many-to-one relationship
    board = db.relationship('Board', backref='fields')  # One-to-many relationship

    def __repr__(self):
        return f'<Field {self.name}>'
