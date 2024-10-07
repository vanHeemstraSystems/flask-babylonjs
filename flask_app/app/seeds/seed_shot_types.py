#!/usr/bin/env python
from app.extensions import db
from app import ShotType

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

if __name__ == "__main__":
    from app import create_app  # Adjust as necessary
    app = create_app()
    with app.app_context():
        seed_shot_types()
