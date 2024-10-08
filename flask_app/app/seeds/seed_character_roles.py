#!/usr/bin/env python
from app.extensions import db
from app.models.character_role import CharacterRole

def seed_character_roles():
    # Clear existing data (optional)
    db.session.query(CharacterRole).delete()
    db.session.commit()

    # Create new character roles
    new_character_role = CharacterRole(name="Antagonist", description="...")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Protagonist", description="...")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Mentor", description="...")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Love Interest", description="...")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Sidekick", description="...")
    db.session.add(new_character_role)
    db.session.commit()           

    print("Character roles seeded!")   

