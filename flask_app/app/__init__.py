#!/usr/bin/env python
from flask import Flask
from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # from app.posts import bp as posts_bp
    # app.register_blueprint(posts_bp, url_prefix='/posts')

    # from app.questions import bp as questions_bp
    # app.register_blueprint(questions_bp, url_prefix='/questions')

    # from app.scene1 import bp as scene1_bp
    # app.register_blueprint(scene1_bp, url_prefix='/scene1')

    # from app.scene2 import bp as scene2_bp
    # app.register_blueprint(scene2_bp, url_prefix='/scene2')

    # from app.scene3 import bp as scene3_bp
    # app.register_blueprint(scene3_bp, url_prefix='/scene3')

    from app.boards import bp as boards_bp
    app.register_blueprint(boards_bp, url_prefix='/boards')

    from app.cameras import bp as cameras_bp
    app.register_blueprint(cameras_bp, url_prefix='/cameras')

    from app.camera_types import bp as camera_types_bp
    app.register_blueprint(camera_types_bp, url_prefix='/camera_types')

    from app.characters import bp as characters_bp
    app.register_blueprint(characters_bp, url_prefix='/characters')

    from app.character_roles import bp as character_roles_bp
    app.register_blueprint(character_roles_bp, url_prefix='/character_roles')

    from app.fields import bp as fields_bp
    app.register_blueprint(fields_bp, url_prefix='/fields')

    from app.field_types import bp as field_types_bp
    app.register_blueprint(field_types_bp, url_prefix='/field_types')

    from app.games import bp as games_bp
    app.register_blueprint(games_bp, url_prefix='/games')

    from app.lights import bp as lights_bp
    app.register_blueprint(lights_bp, url_prefix='/lights')
    
    from app.light_types import bp as light_types_bp
    app.register_blueprint(light_types_bp, url_prefix='/light_types')

    from app.players import bp as players_bp
    app.register_blueprint(players_bp, url_prefix='/players')

    from app.player_roles import bp as player_roles_bp
    app.register_blueprint(player_roles_bp, url_prefix='/player_roles')

    from app.props import bp as props_bp
    app.register_blueprint(props_bp, url_prefix='/props')

    from app.props import bp as props_bp
    app.register_blueprint(props_bp, url_prefix='/props')   

    from app.scenes import bp as scenes_bp
    app.register_blueprint(scenes_bp, url_prefix='/scenes')

    from app.screenplays import bp as screenplays_bp
    app.register_blueprint(screenplays_bp, url_prefix='/screenplays')

    from app.shots import bp as shots_bp
    app.register_blueprint(shots_bp, url_prefix='/shots')
    
    from app.shot_types import bp as shot_types_bp
    app.register_blueprint(shot_types_bp, url_prefix='/shot_types')

    from app.stories import bp as stories_bp
    app.register_blueprint(stories_bp, url_prefix='/stories')

    from app.tags import bp as tags_bp
    app.register_blueprint(tags_bp, url_prefix='/tags')    

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    from app.user_roles import bp as user_roles_bp
    app.register_blueprint(user_roles_bp, url_prefix='/user_roles')     
    
    # @app.route('/test/')
    # def test_page():
    #     return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
