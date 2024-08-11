import os

from flask import Flask
from config import Config
from Chat_.Controller.chatController import chat_bp

from flask_socketio import SocketIO

socketio = SocketIO()


#TODO: Configuration
def created_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = os.urandom(24)

    app.config['TEMPLATES_AUTO_RELOAD'] = True

    app.register_blueprint(chat_bp)

    socketio.init_app(app)

    return app
