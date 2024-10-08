from flask import render_template, request, redirect, url_for, flash
from models import db, SIMCard


class SIMCardManager:
    def __init__(self, app):
        self.app = app
        self._setup_routes()

    def _setup_routes(self):
        # Отображение списка SIM-карт
        @self.app.route('/')
        def index():
            sim_cards = SIMCard.query.all()
            return render_template('index.html', sim_cards=sim_cards)

        # Добавление новой SIM-карты
        @self.app.route('/add', methods=['GET', 'POST'])
        def add_sim_card():
            if request.method == 'POST':
                number = request.form['number']
                operator = request.form['operator']
                comment = request.form.get('comment', '')

                new_sim_card = SIMCard(number=number, operator=operator, comment=comment)
                db.session.add(new_sim_card)
                db.session.commit()
                flash('SIM-карта добавлена успешно!')
                return redirect(url_for('index'))

            return render_template('add_sim_card.html')

        # Редактирование SIM-карты
        @self.app.route('/edit/<int:id>', methods=['GET', 'POST'])
        def edit_sim_card(id):
            sim_card = SIMCard.query.get_or_404(id)

            if request.method == 'POST':
                sim_card.number = request.form['number']
                sim_card.operator = request.form['operator']
                sim_card.comment = request.form.get('comment', '')
                db.session.commit()
                flash('SIM-карта обновлена!')
                return redirect(url_for('index'))

            return render_template('edit_sim_card.html', sim_card=sim_card)

        # Удаление SIM-карты
        @self.app.route('/delete/<int:id>')
        def delete_sim_card(id):
            sim_card = SIMCard.query.get_or_404(id)
            db.session.delete(sim_card)
            db.session.commit()
            flash('SIM-карта удалена!')
            return redirect(url_for('index'))
