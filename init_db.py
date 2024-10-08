from app_manager import AppManager
from models import db

# Инициализация через класс AppManager
app_manager = AppManager()
app = app_manager.get_app()

with app.app_context():
    db.create_all()
    print("База данных успешно инициализирована.")
