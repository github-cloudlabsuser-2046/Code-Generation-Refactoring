import requests

def obtener_datos_meteorologicos(ciudad, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    print(respuesta.status_code)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        return None

# Reemplaza 'tu_api_key' con tu clave de API de OpenWeatherMap
api_key = '5097261bf94cc9933fbe16b3683bac30'
ciudad = 'Santiago' 
datos = obtener_datos_meteorologicos(ciudad, api_key)

if datos:
    print(f"Ciudad: {datos['name']}")
    print(f"Temperatura: {datos['main']['temp']}°C")
    print(f"Clima: {datos['weather'][0]['description']}")
else:
    print("No se pudieron obtener los datos meteorológicos.")