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

    from app.scenes import bp as scenes_bp
    app.register_blueprint(scenes_bp, url_prefix='/scenes')
    
    # @app.route('/test/')
    # def test_page():
    #     return '<h1>Testing the Flask Application Factory Pattern</h1>'
        
    return app