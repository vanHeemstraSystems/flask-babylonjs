#!/usr/bin/env python
import datetime
from app.extensions import db
from app.models.game import Game

def seed_games():
    # Clear existing data (optional)
    db.session.query(Game).delete()
    db.session.commit()

    # Create a new game
    release_date = datetime.datetime.now()
    new_game = Game(id=1, title="John's Game", description="The Game of John Doe", release_date=release_date, genre="Adventure", board_id=1, story_id=1)
    db.session.add(new_game)
    db.session.commit()

    print("Games seeded!")