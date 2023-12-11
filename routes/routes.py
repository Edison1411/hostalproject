from flask import Blueprint, request, jsonify
from models import TipoHabitacion, Empleados, Habitaciones, Huesped, Reservas, RegistroTransacciones
from models import db 

# Operaciones CRUD para la tabla Reservas
reservas = Blueprint('reservas', __name__)
@reservas.route('/reservas', methods=['POST'])
def create_reserva():
    data = request.json
    nueva_reserva = Reservas(**data)
    db.session.add(nueva_reserva)
    db.session.commit()
    return jsonify({'message': 'Reserva creada exitosamente'})

# READ (todas las reservas)
@reservas.route('/reservas', methods=['GET'])
def get_all_reservas():
    reservas = Reservas.query.all()
    resultado = []
    for reserva in reservas:
        resultado.append({
            'ReservaID': reserva.ReservaID,
            'EmpleadoID': reserva.EmpleadoID,
            'HuespedID': reserva.HuespedID,
            'HabitacionID': reserva.HabitacionID,
            'FechaEntrada': reserva.FechaEntrada.strftime('%Y-%m-%d'),
            'FechaSalida': reserva.FechaSalida.strftime('%Y-%m-%d'),
            'EstatusReserva': reserva.EstatusReserva
        })
    return jsonify({'reservas': resultado})

# READ (una reserva específica)
@reservas.route('/reservas/<int:reserva_id>', methods=['GET'])
def get_reserva(reserva_id):
    reserva = Reservas.query.get(reserva_id)
    if reserva:
        return jsonify({
            'ReservaID': reserva.ReservaID,
            'EmpleadoID': reserva.EmpleadoID,
            'HuespedID': reserva.HuespedID,
            'HabitacionID': reserva.HabitacionID,
            'FechaEntrada': reserva.FechaEntrada.strftime('%Y-%m-%d'),
            'FechaSalida': reserva.FechaSalida.strftime('%Y-%m-%d'),
            'EstatusReserva': reserva.EstatusReserva
        })
    return jsonify({'message': 'Reserva no encontrada'}), 404

# UPDATE
@reservas.route('/reservas/<int:reserva_id>', methods=['PUT'])
def update_reserva(reserva_id):
    reserva = Reservas.query.get(reserva_id)
    if reserva:
        data = request.json
        reserva.EmpleadoID = data.get('EmpleadoID', reserva.EmpleadoID)
        reserva.HuespedID = data.get('HuespedID', reserva.HuespedID)
        reserva.HabitacionID = data.get('HabitacionID', reserva.HabitacionID)
        reserva.FechaEntrada = data.get('FechaEntrada', reserva.FechaEntrada)
        reserva.FechaSalida = data.get('FechaSalida', reserva.FechaSalida)
        reserva.EstatusReserva = data.get('EstatusReserva', reserva.EstatusReserva)
        db.session.commit()
        return jsonify({'message': 'Reserva actualizada exitosamente'})
    return jsonify({'message': 'Reserva no encontrada'}), 404

# DELETE
@reservas.route('/reservas/<int:reserva_id>', methods=['DELETE'])
def delete_reserva(reserva_id):
    reserva = Reservas.query.get(reserva_id)
    if reserva:
        db.session.delete(reserva)
        db.session.commit()
        return jsonify({'message': 'Reserva eliminada exitosamente'})
    return jsonify({'message': 'Reserva no encontrada'}), 404


# Operaciones CRUD para la tabla Empleados
empleados = Blueprint('empleados', __name__)
# CREATE
@empleados.route('/empleados', methods=['POST'])
def create_empleado():
    data = request.json
    nuevo_empleado = Empleados(**data)
    db.session.add(nuevo_empleado)
    db.session.commit()
    return jsonify({'message': 'Empleado creado exitosamente'})

# READ (todos los empleados)
@empleados.route('/empleados', methods=['GET'])
def get_all_empleados():
    empleados = Empleados.query.all()
    resultado = []
    for empleado in empleados:
        resultado.append({
            'EmpleadoID': empleado.EmpleadoID,
            'NombreE': empleado.NombreE,
            'CargoE': empleado.CargoE,
            'ContactoE': empleado.ContactoE,
            'SalarioE': empleado.SalarioE,
            'FechaContratacion': empleado.FechaContratacion.strftime('%Y-%m-%d'),
            'TipoEmpleado': empleado.TipoEmpleado
        })
    return jsonify({'empleados': resultado})

# READ (un empleado específico)
@empleados.route('/empleados/<int:empleado_id>', methods=['GET'])
def get_empleado(empleado_id):
    empleado = Empleados.query.get(empleado_id)
    if empleado:
        return jsonify({
            'EmpleadoID': empleado.EmpleadoID,
            'NombreE': empleado.NombreE,
            'CargoE': empleado.CargoE,
            'ContactoE': empleado.ContactoE,
            'SalarioE': empleado.SalarioE,
            'FechaContratacion': empleado.FechaContratacion.strftime('%Y-%m-%d'),
            'TipoEmpleado': empleado.TipoEmpleado
        })
    return jsonify({'message': 'Empleado no encontrado'}), 404

# UPDATE
@empleados.route('/empleados/<int:empleado_id>', methods=['PUT'])
def update_empleado(empleado_id):
    empleado = Empleados.query.get(empleado_id)
    if empleado:
        data = request.json
        empleado.NombreE = data.get('NombreE', empleado.NombreE)
        empleado.CargoE = data.get('CargoE', empleado.CargoE)
        empleado.ContactoE = data.get('ContactoE', empleado.ContactoE)
        empleado.SalarioE = data.get('SalarioE', empleado.SalarioE)
        empleado.FechaContratacion = data.get('FechaContratacion', empleado.FechaContratacion)
        empleado.TipoEmpleado = data.get('TipoEmpleado', empleado.TipoEmpleado)
        db.session.commit()
        return jsonify({'message': 'Empleado actualizado exitosamente'})
    return jsonify({'message': 'Empleado no encontrado'}), 404

# DELETE
@empleados.route('/empleados/<int:empleado_id>', methods=['DELETE'])
def delete_empleado(empleado_id):
    empleado = Empleados.query.get(empleado_id)
    if empleado:
        db.session.delete(empleado)
        db.session.commit()
        return jsonify({'message': 'Empleado eliminado exitosamente'})
    return jsonify({'message': 'Empleado no encontrado'}), 404

# operaciones CRUD para la tabla Habitaciones
#Create
habitaciones = Blueprint('habitaciones', __name__)
@habitaciones.route('/habitaciones', methods=['POST'])
def create_habitacion():
    data = request.json
    nueva_habitacion = Habitaciones(**data)
    db.session.add(nueva_habitacion)
    db.session.commit()
    return jsonify({'message': 'Habitación creada exitosamente'})

# READ (todas las habitaciones)
@habitaciones.route('/habitaciones', methods=['GET'])
def get_all_habitaciones():
    habitaciones = Habitaciones.query.all()
    resultado = []
    for habitacion in habitaciones:
        resultado.append({
            'HabitacionID': habitacion.HabitacionID,
            'EmpleadoID': habitacion.EmpleadoID,
            'TipoHabID': habitacion.TipoHabID,
            'EstatusHabitacion': habitacion.EstatusHabitacion
        })
    return jsonify({'habitaciones': resultado})

# READ (una habitación específica)
@habitaciones.route('/habitaciones/<string:habitacion_id>', methods=['GET'])
def get_habitacion(habitacion_id):
    habitacion = Habitaciones.query.get(habitacion_id)
    if habitacion:
        return jsonify({
            'HabitacionID': habitacion.HabitacionID,
            'EmpleadoID': habitacion.EmpleadoID,
            'TipoHabID': habitacion.TipoHabID,
            'EstatusHabitacion': habitacion.EstatusHabitacion
        })
    return jsonify({'message': 'Habitación no encontrada'}), 404

# UPDATE
@habitaciones.route('/habitaciones/<string:habitacion_id>', methods=['PUT'])
def update_habitacion(habitacion_id):
    habitacion = Habitaciones.query.get(habitacion_id)
    if habitacion:
        data = request.json
        habitacion.EmpleadoID = data.get('EmpleadoID', habitacion.EmpleadoID)
        habitacion.TipoHabID = data.get('TipoHabID', habitacion.TipoHabID)
        habitacion.EstatusHabitacion = data.get('EstatusHabitacion', habitacion.EstatusHabitacion)
        db.session.commit()
        return jsonify({'message': 'Habitación actualizada exitosamente'})
    return jsonify({'message': 'Habitación no encontrada'}), 404

# DELETE
@habitaciones.route('/habitaciones/<string:habitacion_id>', methods=['DELETE'])
def delete_habitacion(habitacion_id):
    habitacion = Habitaciones.query.get(habitacion_id)
    if habitacion:
        db.session.delete(habitacion)
        db.session.commit()
        return jsonify({'message': 'Habitación eliminada exitosamente'})
    return jsonify({'message': 'Habitación no encontrada'}), 404

huespedes = Blueprint('huespedes', __name__)

# operaciones CRUD para la tabla Huesped
@huespedes.route('/huespedes', methods=['POST'])
def create_huesped():
    data = request.json
    nuevo_huesped = Huesped(**data)
    db.session.add(nuevo_huesped)
    db.session.commit()
    return jsonify({'message': 'Huésped creado exitosamente'})

# READ (todos los huéspedes)
@huespedes.route('/huespedes', methods=['GET'])
def get_all_huespedes():
    huespedes = Huesped.query.all()
    resultado = []
    for huesped in huespedes:
        resultado.append({
            'HuespedID': huesped.HuespedID,
            'Telefono': huesped.Telefono,
            'CorreoElectronico': huesped.CorreoElectronico,
            'Direccion': huesped.Direccion,
            'Nombre': huesped.Nombre
        })
    return jsonify({'huespedes': resultado})

# READ (un huésped específico)
@huespedes.route('/huespedes/<int:huesped_id>', methods=['GET'])
def get_huesped(huesped_id):
    huesped = Huesped.query.get(huesped_id)
    if huesped:
        return jsonify({
            'HuespedID': huesped.HuespedID,
            'Telefono': huesped.Telefono,
            'CorreoElectronico': huesped.CorreoElectronico,
            'Direccion': huesped.Direccion,
            'Nombre': huesped.Nombre
        })
    return jsonify({'message': 'Huésped no encontrado'}), 404

# UPDATE
@huespedes.route('/huespedes/<int:huesped_id>', methods=['PUT'])
def update_huesped(huesped_id):
    huesped = Huesped.query.get(huesped_id)
    if huesped:
        data = request.json
        huesped.Telefono = data.get('Telefono', huesped.Telefono)
        huesped.CorreoElectronico = data.get('CorreoElectronico', huesped.CorreoElectronico)
        huesped.Direccion = data.get('Direccion', huesped.Direccion)
        huesped.Nombre = data.get('Nombre', huesped.Nombre)
        db.session.commit()
        return jsonify({'message': 'Huésped actualizado exitosamente'})
    return jsonify({'message': 'Huésped no encontrado'}), 404

# DELETE
@huespedes.route('/huespedes/<int:huesped_id>', methods=['DELETE'])
def delete_huesped(huesped_id):
    huesped = Huesped.query.get(huesped_id)
    if huesped:
        db.session.delete(huesped)
        db.session.commit()
        return jsonify({'message': 'Huésped eliminado exitosamente'})
    return jsonify({'message': 'Huésped no encontrado'}), 404

# Operaciones CRUD para la tabla TipoHabitacion
tipoahabitacion = Blueprint('tipo_habitacion', __name__)
# CREATE
@tipoahabitacion.route('/tipo_habitacion', methods=['POST'])
def create_tipo_habitacion():
    data = request.json
    new_tipo_habitacion = TipoHabitacion(**data)
    db.session.add(new_tipo_habitacion)
    db.session.commit()
    return jsonify({'message': 'Tipo de habitación creado exitosamente'})


# READ

@tipoahabitacion.route('/tipo_habitacion/<int:tipo_hab_id>', methods=['GET'])
def get_tipo_habitacion(tipo_hab_id):
    tipo_habitacion = TipoHabitacion.query.get(tipo_hab_id)
    if tipo_habitacion:
        tipo_habitacion_dict = {
            'TipoHabID': tipo_habitacion.TipoHabID,
            'TipoHab': tipo_habitacion.TipoHab,
            'DescripcionHab': tipo_habitacion.DescripcionHab,
            'TarifaNoche': tipo_habitacion.TarifaNoche
        }
        return jsonify(tipo_habitacion_dict)
    return jsonify({'message': 'Tipo de habitación no encontrado'}), 404

# UPDATE
@tipoahabitacion.route('/tipo_habitacion/<int:tipo_hab_id>', methods=['PUT'])
def update_tipo_habitacion(tipo_hab_id):
    tipo_habitacion = TipoHabitacion.query.get(tipo_hab_id)
    if tipo_habitacion:
        data = request.json
        tipo_habitacion.TipoHab = data.get('TipoHab', tipo_habitacion.TipoHab)
        tipo_habitacion.DescripcionHab = data.get('DescripcionHab', tipo_habitacion.DescripcionHab)
        tipo_habitacion.TarifaNoche = data.get('TarifaNoche', tipo_habitacion.TarifaNoche)
        db.session.commit()
        return jsonify({'message': 'Tipo de habitación actualizado exitosamente'})
    return jsonify({'message': 'Tipo de habitación no encontrado'}), 404

# DELETE
@tipoahabitacion.route('/tipo_habitacion/<int:tipo_hab_id>', methods=['DELETE'])
def delete_tipo_habitacion(tipo_hab_id):
    tipo_habitacion = TipoHabitacion.query.get(tipo_hab_id)
    if tipo_habitacion:
        db.session.delete(tipo_habitacion)
        db.session.commit()
        return jsonify({'message': 'Tipo de habitación eliminado exitosamente'})
    return jsonify({'message': 'Tipo de habitación no encontrado'}), 404

from flask import Blueprint, request, jsonify
transacciones = Blueprint('transacciones', __name__)
# Operaciones CRUD para la tabla RegistroTransacciones
@transacciones.route('/transacciones', methods=['POST'])
def create_transaccion():
    data = request.json
    nueva_transaccion = Transacciones(**data)
    db.session.add(nueva_transaccion)
    db.session.commit()
    return jsonify({'message': 'Transacción creada exitosamente'})

# READ (todas las transacciones)
@transacciones.route('/transacciones', methods=['GET'])
def get_all_transacciones():
    transacciones = RegistroTransacciones.query.all()
    resultado = []
    for transaccion in transacciones:
        resultado.append({
            'TransaccionID': transaccion.TransaccionID,
            'ReservaID': transaccion.ReservaID,
            'Monto': transaccion.Monto,
            'FechaTransaccion': transaccion.FechaTransaccion.strftime('%Y-%m-%d')
        })
    return jsonify({'transacciones': resultado})

# READ (una transacción específica)
@transacciones.route('/transacciones/<int:transaccion_id>', methods=['GET'])
def get_transaccion(transaccion_id):
    transaccion = RegistroTransacciones.query.get(transaccion_id)
    if transaccion:
        return jsonify({
            'TransaccionID': transaccion.TransaccionID,
            'ReservaID': transaccion.ReservaID,
            'Monto': transaccion.Monto,
            'FechaTransaccion': transaccion.FechaTransaccion.strftime('%Y-%m-%d')
        })
    return jsonify({'message': 'Transacción no encontrada'}), 404

# UPDATE
@transacciones.route('/transacciones/<int:transaccion_id>', methods=['PUT'])
def update_transaccion(transaccion_id):
    transaccion = RegistroTransacciones.query.get(transaccion_id)
    if transaccion:
        data = request.json
        transaccion.ReservaID = data.get('ReservaID', transaccion.ReservaID)
        transaccion.Monto = data.get('Monto', transaccion.Monto)
        transaccion.FechaTransaccion = data.get('FechaTransaccion', transaccion.FechaTransaccion)
        db.session.commit()
        return jsonify({'message': 'Transacción actualizada exitosamente'})
    return jsonify({'message': 'Transacción no encontrada'}), 404

# DELETE
@transacciones.route('/transacciones/<int:transaccion_id>', methods=['DELETE'])
def delete_transaccion(transaccion_id):
    transaccion = RegistroTransacciones.query.get(transaccion_id)
    if transaccion:
        db.session.delete(transaccion)
        db.session.commit()
        return jsonify({'message': 'Transacción eliminada exitosamente'})
    return jsonify({'message': 'Transacción no encontrada'}), 404
