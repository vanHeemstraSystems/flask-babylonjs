#!/usr/bin/env python
from app.extensions import db

class Prop(db.Model):
    __tablename__ = 'prop'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model_url = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Prop {self.name}>'   
