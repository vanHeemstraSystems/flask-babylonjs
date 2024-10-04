#!/usr/bin/env python
from app.extensions import db

class Scene3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Scene3 "{self.title}">'