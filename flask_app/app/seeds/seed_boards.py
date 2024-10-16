#!/usr/bin/env python
from app.extensions import db
from app.models.board import Board

def seed_boards():
    # Clear existing data (optional)
    db.session.query(Board).delete()
    db.session.commit()

    # Create a new board
    new_board = Board(name="John's Board", description="The Board of John Doe")
    db.session.add(new_board)
    db.session.commit()

    print("Boards seeded!")