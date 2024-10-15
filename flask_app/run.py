#!/usr/bin/env python
import os
from app import create_app
from app.extensions import db, socketio
from app.seeds.seed_camera_types import seed_camera_types
from app.seeds.seed_character_roles import seed_character_roles
from app.seeds.seed_character_types import seed_character_types
from app.seeds.seed_field_types import seed_field_types
from app.seeds.seed_fields import seed_fields
from app.seeds.seed_light_types import seed_light_types
from app.seeds.seed_player_roles import seed_player_roles
from app.seeds.seed_shot_types import seed_shot_types
from app.seeds.seed_stories import seed_stories
from app.seeds.seed_user_roles import seed_user_roles

app = create_app()

if __name__ == "__main__":
    socketio.run(app)
    with app.app_context():
        db.create_all()
        # seed_camera_types()
        # seed_character_roles()
        # seed_character_types()        
        # seed_field_types()
        # seed_fields()
        # seed_light_types()
        # seed_player_roles()
        # seed_shot_types()        
        # seed_stories()
        # seed_user_roles()