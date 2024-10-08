#!/usr/bin/env python
import os
from app import create_app
from app.extensions import db, socketio
from app.seeds.seed_camera_types import seed_camera_types
from app.seeds.seed_cameras import seed_cameras
from app.seeds.seed_character_roles import seed_character_roles
from app.seeds.seed_field_types import seed_field_types
from app.seeds.seed_fields import seed_fields
from app.seeds.seed_player_roles import seed_player_roles
from app.seeds.seed_shot_types import seed_shot_types
from app.seeds.seed_stories import seed_stories

app = create_app()

if __name__ == "__main__":
    socketio.run(app)
    with app.app_context():
        seed_camera_types()
        seed_cameras()
        seed_character_roles()
        seed_field_types()
        seed_fields()
        seed_player_roles()
        seed_shot_types()        
        seed_stories()