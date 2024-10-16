#!/usr/bin/env python
from app.extensions import db
from app.models.game import Game

def seed_games():
    # Clear existing data (optional)
    db.session.query(Game).delete()
    db.session.commit()

    # Create a new game
    new_game = Game(title="John's Game", description="The Game of John Doe", release_date="1-1-1979", genre="Adventure", story_id=1)
    db.session.add(new_game)
    db.session.commit()

    print("Games seeded!")