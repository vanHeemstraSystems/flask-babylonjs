#!/usr/bin/env python
from app.extensions import db
from app.models.user_role import UserRole

def seed_user_roles():
    # Clear existing data (optional)
    db.session.query(UserRole).delete()
    db.session.commit()

    # Create new user roles
    new_user_role = UserRole(name="Player", description="...")
    db.session.add(new_user_role)
    db.session.commit()

    new_user_role = UserRole(name="Viewer", description="...")
    db.session.add(new_user_role)
    db.session.commit()

    new_user_role = UserRole(name="Editor", description="...")
    db.session.add(new_user_role)
    db.session.commit()

    new_user_role = UserRole(name="Administrator", description="...")
    db.session.add(new_user_role)
    db.session.commit()        

    print("User roles seeded!")      