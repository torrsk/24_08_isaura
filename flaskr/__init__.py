from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY DATABASE_URI'] = 'sqlite:///tutorial_canciones.db'
    app.config['SQLALCAHEMY_TRACK_MODIFICATIONS'] = False
    return app