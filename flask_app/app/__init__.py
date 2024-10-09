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
    from app.routes.main_routes import bp as main_bp
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

    # from app.routes.board_routes import bp as board_bp
    # app.register_blueprint(board_bp, url_prefix='/boards')

    # from app.routes.camera_routes import bp as camera_bp
    # app.register_blueprint(camera_bp, url_prefix='/cameras')

    # from app.routes.camera_type_routes import bp as camera_type_bp
    # app.register_blueprint(camera_type_bp, url_prefix='/camera_types')

    # from app.routes.character_routes import bp as character_bp
    # app.register_blueprint(character_bp, url_prefix='/characters')

    # from app.routes.character_role_routes import bp as character_role_bp
    # app.register_blueprint(character_role_bp, url_prefix='/character_roles')

    # from app.routes.character_type_routes import bp as character_type_bp
    # app.register_blueprint(character_type_bp, url_prefix='/character_types')    

    # from app.routes.field_routes import bp as field_bp
    # app.register_blueprint(field_bp, url_prefix='/fields')

    # from app.routes.field_type_routes import bp as field_type_bp
    # app.register_blueprint(field_type_bp, url_prefix='/field_types')

    # from app.routes.game_routes import bp as game_bp
    # app.register_blueprint(game_bp, url_prefix='/games')

    # from app.routes.light_routes import bp as light_bp
    # app.register_blueprint(light_bp, url_prefix='/lights')
    
    # from app.routes.light_type_routes import bp as light_type_bp
    # app.register_blueprint(light_type_bp, url_prefix='/light_types')

    # from app.routes.player_routes import bp as player_bp
    # app.register_blueprint(player_bp, url_prefix='/players')

    # from app.routes.player_role_routes import bp as player_role_bp
    # app.register_blueprint(player_role_bp, url_prefix='/player_roles')

    # from app.routes.prop_routes import bp as prop_bp
    # app.register_blueprint(prop_bp, url_prefix='/props')  

    # from app.routes.scene_routes import bp as scene_bp
    # app.register_blueprint(scene_bp, url_prefix='/scenes')

    # from app.routes.screenplay_routes import bp as screenplay_bp
    # app.register_blueprint(screenplay_bp, url_prefix='/screenplays')

    # from app.routes.shot_routes import bp as shot_bp
    # app.register_blueprint(shot_bp, url_prefix='/shots')
    
    # from app.routes.shot_type_routes import bp as shot_type_bp
    # app.register_blueprint(shot_type_bp, url_prefix='/shot_types')

    # from app.routes.story_routes import bp as story_bp
    # app.register_blueprint(story_bp, url_prefix='/stories')

    # from app.routes.tag_routes import bp as tag_bp
    # app.register_blueprint(tag_bp, url_prefix='/tags')    

    # from app.routes.user_routes import bp as user_bp
    # app.register_blueprint(user_bp, url_prefix='/users')

    # from app.routes.user_role_routes import bp as user_role_bp
    # app.register_blueprint(user_role_bp, url_prefix='/user_roles')     
    
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
