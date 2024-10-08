#!/usr/bin/env python
from app.extensions import db
from app.models.player_role import PlayerRole

def seed_player_roles():
    player_roles = [
        'Product Owner',
        'Scrum Master',
        'Security Expert',
        'Architect',
        'Engineer',
        'Stakeholder'
    ]

    # Clear existing data (optional)
    db.session.query(PlayerRole).delete()
    db.session.commit()

    for name in player_roles:
        player_role = PlayerRole(name=name)
        db.session.add(player_role)

    db.session.commit()
    print("Player roles seeded!")