#!/usr/bin/env python
from app.extensions import db
from app.models.user import User

def seed_users():
    # Clear existing data (optional)
    db.session.query(User).delete()
    db.session.commit()
 
    # Create a new user
    new_user = User(id=1, username="johndoe", email="john.doe@example.com", password_hash="secret")
    db.session.add(new_user)
    db.session.commit()

    print("Users seeded!")