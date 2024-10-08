from flask import Flask
from models import db
from config import Config

class AppManager:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        self._setup_database()

    def _setup_database(self):
        db.init_app(self.app)

    def get_app(self):
        return self.app
