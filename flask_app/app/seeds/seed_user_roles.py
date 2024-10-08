#!/usr/bin/env python
from app.extensions import db
from app.models.user_role import UserRole

def seed_user_roles():
    user_roles = [
        'Player',
        'Viewer',
        'Editor',
        'Administrator'
    ]

    # Clear existing data (optional)
    db.session.query(UserRole).delete()
    db.session.commit()

    for name in user_roles:
        user_role = UserRole(name=name)
        db.session.add(user_role)

    db.session.commit()
    print("User roles seeded!")