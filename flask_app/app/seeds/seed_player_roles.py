#!/usr/bin/env python
from app.extensions import db
from app.models.player_role import PlayerRole

def seed_player_roles():
    # Clear existing data (optional)
    db.session.query(PlayerRole).delete()
    db.session.commit()

    # Create new player roles
    new_player_role = PlayerRole(name="Product Owner", description="...")
    db.session.add(new_player_role)
    db.session.commit()

    new_player_role = PlayerRole(name="Scrum Master", description="...")
    db.session.add(new_player_role)
    db.session.commit()

    new_player_role = PlayerRole(name="Security Expert", description="...")
    db.session.add(new_player_role)
    db.session.commit()

    new_player_role = PlayerRole(name="Architect", description="...")
    db.session.add(new_player_role)
    db.session.commit()

    new_player_role = PlayerRole(name="Engineer", description="...")
    db.session.add(new_player_role)
    db.session.commit()

    new_player_role = PlayerRole(name="Stakeholder", description="...")
    db.session.add(new_player_role)
    db.session.commit()              

    print("Player roles seeded!")      