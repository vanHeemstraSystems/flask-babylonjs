#!/usr/bin/env python
from app.extensions import db
from app.models.story import Story

def seed_stories():
    # Clear existing data (optional)
    db.session.query(Story).delete()
    db.session.commit()

    # Create a new story
    new_story = Story(id=1, title="Agility", content="A story about agility and quickness in movement.")
    db.session.add(new_story)
    db.session.commit()

    print("Stories seeded!")

