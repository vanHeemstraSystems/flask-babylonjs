#!/usr/bin/env python
from app.extensions import db
from app.models.profile import Profile

def seed_profiles():
    # Clear existing data (optional)
    db.session.query(Profile).delete()
    db.session.commit()

    # Create a new profile
    new_profile = Profile(id=1, profilename="John Doe", user_id=1)
    db.session.add(new_profile)
    db.session.commit()

    print("Profiles seeded!")