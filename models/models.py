from . import db


class TipoHabitacion(db.Model):
    TipoHabID = db.Column(db.Integer, primary_key=True)
    TipoHab = db.Column(db.String(20), nullable=False)
    DescripcionHab = db.Column(db.String(100) , nullable=False)
    TarifaNoche = db.Column(db.Integer, nullable=False)

class Empleados(db.Model):
    EmpleadoID = db.Column(db.Integer, primary_key=True)
    NombreE = db.Column(db.String(50), nullable=False)
    CargoE = db.Column(db.String(20), nullable=False)
    ContactoE = db.Column(db.String(15), nullable=False)
    SalarioE = db.Column(db.Integer, nullable=False)
    FechaContratacion = db.Column(db.Date, nullable=False)
    TipoEmpleado = db.Column(db.String(50), nullable=False)

class Habitaciones(db.Model):
    HabitacionID = db.Column(db.String(50), primary_key=True)
    EmpleadoID = db.Column(db.Integer, db.ForeignKey('empleados.EmpleadoID'), nullable=False)
    TipoHabID = db.Column(db.Integer, db.ForeignKey('tipo_habitacion.TipoHabID'), nullable=False)
    EstatusHabitacion = db.Column(db.String(50), nullable=False)

class Huesped(db.Model):
    HuespedID = db.Column(db.Integer, primary_key=True)
    Telefono = db.Column(db.String(10), nullable=False)
    CorreoElectronico = db.Column(db.String(200), nullable=False)
    Direccion = db.Column(db.String(100), nullable=False)
    Nombre = db.Column(db.String(100), nullable=False)

class Reservas(db.Model):
    ReservaID = db.Column(db.Integer, primary_key=True)
    EmpleadoID = db.Column(db.Integer, db.ForeignKey('empleados.EmpleadoID'), nullable=False)
    HuespedID = db.Column(db.Integer, db.ForeignKey('huesped.HuespedID'), nullable=False)
    HabitacionID = db.Column(db.String(50), db.ForeignKey('habitaciones.HabitacionID'), nullable=False)
    FechaEntrada = db.Column(db.Date, nullable=False)
    FechaSalida = db.Column(db.Date, nullable=False)
    EstatusReserva = db.Column(db.String(50), nullable=False)

class RegistroTransacciones(db.Model):
    TransaccionID = db.Column(db.Integer, primary_key=True)
    ReservaID = db.Column(db.Integer, db.ForeignKey('reservas.ReservaID'), nullable=False)
    Monto = db.Column(db.Integer, nullable=False)
    FechaTransaccion = db.Column(db.Date, nullable=False)
