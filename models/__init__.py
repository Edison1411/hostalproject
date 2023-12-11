from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models import TipoHabitacion, Empleados, Habitaciones, Huesped, Reservas, RegistroTransacciones
