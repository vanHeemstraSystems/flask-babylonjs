#!/usr/bin/env python
from app.extensions import db

class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    profilename = db.Column(db.String(100), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    user = db.relationship('User', back_populates='profile')  # Relationship with User

    def __repr__(self):
        return f'<Profile {self.profilename}>'
 