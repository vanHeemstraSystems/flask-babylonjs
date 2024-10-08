#!/usr/bin/env python
from app.extensions import db
from app.models.shot_type import ShotType

def seed_shot_types():
    shot_types = [
        'Wide Shot',
        'Close-Up',
        'Medium Shot',
        'Dolly Shot',
        'Tracking Shot'
    ]

    # Clear existing data (optional)
    db.session.query(ShotType).delete()
    db.session.commit()

    for name in shot_types:
        shot_type = ShotType(name=name)
        db.session.add(shot_type)

    db.session.commit()
    print("Shot types seeded!")

