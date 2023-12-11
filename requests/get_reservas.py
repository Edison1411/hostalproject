import requests

# URL de la aplicación Flask (asegúrate de tener el servidor Flask en ejecución)
url = "http://127.0.0.1:5000/reservas"

# Realizar la solicitud GET
response = requests.get(url)

# Imprimir la respuesta del servidor
print(response.status_code)
print(response.json())
