from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SIMCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), unique=True, nullable=False)
    operator = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default="Active")
    comment = db.Column(db.String(200), nullable=True)
