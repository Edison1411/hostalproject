# Hotel Management System

Este es un sistema de gestión de hotel desarrollado con Flask y SQLAlchemy.

## Requisitos Previos

Asegúrate de tener instalado Python y las dependencias del proyecto. Puedes instalar las dependencias ejecutando:
```
bash
pip install -r requirements.txt
```
Configuración

Ajusta la configuración del proyecto según tus necesidades en el archivo config.py.
Iniciar la Aplicación

Ejecuta el siguiente comando para iniciar la aplicación:

```
bash

python app.py
```
La aplicación estará disponible en http://127.0.0.1:5000.
Endpoints API
Tipo de Habitación

    Crear Tipo de Habitación: POST /tipo_habitacion
        Crea un nuevo tipo de habitación.

    Obtener Todos los Tipos de Habitación: GET /tipo_habitacion
        Obtiene todos los tipos de habitación.

    Obtener Detalles de un Tipo de Habitación: GET /tipo_habitacion/<tipo_hab_id>
        Obtiene detalles de un tipo de habitación específico.

Reservas

    Crear Reserva: POST /reservas
        Crea una nueva reserva.

    Obtener Todas las Reservas: GET /reservas
        Obtiene todas las reservas.

    Obtener Detalles de una Reserva: GET /reservas/<reserva_id>
        Obtiene detalles de una reserva específica.

    Actualizar Reserva: PUT /reservas/<reserva_id>
        Actualiza una reserva existente.

    Eliminar Reserva: DELETE /reservas/<reserva_id>
        Elimina una reserva existente.
