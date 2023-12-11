from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from routes.routes import reservas, empleados, habitaciones, huespedes, tipoahabitacion, transacciones
from config import DatabaseConfig


app = Flask(__name__)
app.config.from_object(DatabaseConfig)

# Inicializa Flask-SQLAlchemy con la aplicación
db.init_app(app)

# Registra los blueprints
app.register_blueprint(reservas)
app.register_blueprint(empleados)
app.register_blueprint(habitaciones)
app.register_blueprint(huespedes)
app.register_blueprint(tipoahabitacion)
app.register_blueprint(transacciones)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)
