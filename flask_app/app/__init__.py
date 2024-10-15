#!/usr/bin/env python
from flask import Flask
from config import Config
from app.extensions import db, bcrypt, login_manager, socketio

def create_app(config_class=Config):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(config_class)

    ##
    # Initialize Flask extensions
    ##

    # Set db
    db.init_app(app)

    # Set bycrypt
    bcrypt.init_app(app)

    # Set login manager
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Set socket io
    socketio.init_app(app)
    socketio.cors_allowed_origins = "*"    

    ##
    # Register blueprints
    ##

    # from app.routes.avatar_routes import avatar_bp
    # app.register_blueprint(avatar_bp)

    from app.routes.main_routes import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    # from app.routes.board_routes import board_bp
    # app.register_blueprint(board_bp, url_prefix='/boards')

    # from app.routes.camera_routes import camera_bp
    # app.register_blueprint(camera_bp, url_prefix='/cameras')

    # from app.routes.camera_type_routes import camera_type_bp
    # app.register_blueprint(camera_type_bp, url_prefix='/camera_types')

    # from app.routes.character_routes import character_bp
    # app.register_blueprint(character_bp, url_prefix='/characters')

    # from app.routes.character_role_routes import character_role_bp
    # app.register_blueprint(character_role_bp, url_prefix='/character_roles')

    # from app.routes.character_type_routes import character_type_bp
    # app.register_blueprint(character_type_bp, url_prefix='/character_types')    

    # from app.routes.field_routes import field_bp
    # app.register_blueprint(field_bp, url_prefix='/fields')

    # from app.routes.field_type_routes import field_type_bp
    # app.register_blueprint(field_type_bp, url_prefix='/field_types')

    # from app.routes.game_routes import game_bp
    # app.register_blueprint(game_bp, url_prefix='/games')

    # from app.routes.light_routes import light_bp
    # app.register_blueprint(light_bp, url_prefix='/lights')
    
    # from app.routes.light_type_routes import light_type_bp
    # app.register_blueprint(light_type_bp, url_prefix='/light_types')

    from app.routes.login_routes import login_bp
    app.register_blueprint(login_bp, url_prefix='/login') 

    # from app.routes.player_routes import player_bp
    # app.register_blueprint(player_bp, url_prefix='/players')

    # from app.routes.player_role_routes import player_role_bp
    # app.register_blueprint(player_role_bp, url_prefix='/player_roles')

    # from app.routes.prop_routes import prop_bp
    # app.register_blueprint(prop_bp, url_prefix='/props')  

    from app.routes.registration_routes import registration_bp
    app.register_blueprint(registration_bp, url_prefix='/registration') 

    # from app.routes.scene_routes import scene_bp
    # app.register_blueprint(scene_bp, url_prefix='/scenes')

    # from app.routes.screenplay_routes import screenplay_bp
    # app.register_blueprint(screenplay_bp, url_prefix='/screenplays')

    # from app.routes.shot_routes import shot_bp
    # app.register_blueprint(shot_bp, url_prefix='/shots')
    
    # from app.routes.shot_type_routes import shot_type_bp
    # app.register_blueprint(shot_type_bp, url_prefix='/shot_types')

    # from app.routes.story_routes import story_bp
    # app.register_blueprint(story_bp, url_prefix='/stories')

    # from app.routes.tag_routes import tag_bp
    # app.register_blueprint(tag_bp, url_prefix='/tags')    

    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/users')

    # from app.routes.user_role_routes import user_role_bp
    # app.register_blueprint(user_role_bp, url_prefix='/user_roles')     
    
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
