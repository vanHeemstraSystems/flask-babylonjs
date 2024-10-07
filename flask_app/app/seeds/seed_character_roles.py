#!/usr/bin/env python
from app.extensions import db
from app import CharacterRole

def seed_character_roles():
    character_roles = [
        'Antagonist',
        'Protagonist',
        'Mentor',
        'Love Interest',
        'Sidekick'
    ]

    # Clear existing data (optional)
    db.session.query(CharacterRole).delete()
    db.session.commit()

    for name in character_roles:
        character_role = CharacterRole(name=name)
        db.session.add(character_role)

    db.session.commit()
    print("Character roles seeded!")

if __name__ == "__main__":
    from app import create_app  # Adjust as necessary
    app = create_app()
    with app.app_context():
        seed_character_roles()
