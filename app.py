from flask import Flask, render_template, request, redirect, url_for, flash
from app_manager import AppManager  # Импорт класса для управления приложением
from sim_card_manager import SIMCardManager  # Импорт класса для управления маршрутами SIM-карт

# Инициализация приложения через AppManager
app_manager = AppManager()
app = app_manager.get_app()

# Инициализация маршрутов для работы с SIM-картами
sim_manager = SIMCardManager(app)

if __name__ == '__main__':
    app.run(debug=True)
