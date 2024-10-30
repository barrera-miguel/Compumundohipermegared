import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def mostrar_portada():
    print("-----------------------------")
    print("--------APP DEL CLIMA--------")
    print("by Compumundohipermegared")
    print("-----------------------------")

def seleccionar_unidad():
    while True:
        unidad = input("Selecciona la unidad  de temperatura (C para Celsius, F para Fahrenheit): ").strip().lower()
        if unidad == 'c':
            return 'metric', '°C'
        elif unidad == 'f':
            return 'imperial', '°F'
        else:
            print("-----------------------------")
            print("Entrada no válida. Intente nuevamente")
            print("-----------------------------")
        
def ingresar_ciudad():
    while True:
        ciudad = input("Ingrese una ciudad: ").strip().title()
        if ciudad.isdigit() or len(ciudad) == 0:
            print("-----------------------------")
            print("Entrada no válida. Intente nuevamente")
            print("-----------------------------")
        else:
            return ciudad

def solicitar_clima(ciudad, API_KEY, units):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units={units}&lang=es"
    res = requests.get(url)
    return res.json()

def mostrar_clima_actual(data, ciudad, simbolo):
    temp = data["main"]["temp"]
    descripcion = data["weather"] [0] ["description"]
    minima = data["main"]["temp_min"]
    maxima = data["main"]["temp_max"]
    humedad = data["main"]["humidity"]
    print("-----------------------------")
    print(f'Temperatura actual en {ciudad}: {temp} {simbolo}')
    print(f'Temperatura máxima: {maxima} {simbolo}')
    print(f'Temperatura mínima: {minima} {simbolo}')
    print(f"Humedad: {humedad} %")
    print(f"Descripción: {descripcion}")
    print("-----------------------------")

def preguntar_pronostico():
    while True:
        opcion = input("¿Quiere ver el pronóstico extendido a 5 días? (ingrese 's' para sí o 'n' para no): ").strip().lower()
        if opcion in ('s', 'n'):
            return opcion == 's'
        print("-----------------------------")
        print("Opción no válida. Intente nuevamente")
        print("-----------------------------")

def solicitar_clima_extendido(ciudad, API_KEY, units):
    url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={API_KEY}&units={units}&lang=es"
    res_forecast = requests.get(url_forecast)
    return res_forecast.json()

def mostrar_pronostico_extendido(data_forecast, simbolo):
    print("-------Pronóstico Extendido a 5 Días-------")
    for forecast in data_forecast['list']:
        fecha = forecast['dt_txt']
        temp_forecast = forecast['main']['temp']
        hum_forecast = forecast["main"]["humidity"]
        desc_forecast = forecast['weather'][0]['description']
        print(f"{fecha}: {temp_forecast} {simbolo}, Humedad: {hum_forecast} %, {desc_forecast}")
    print("------------------------------------------")

def realizar_nueva_consulta():
    while True:
        opcion = input("¿Quiere hacer otra consulta? (ingrese 's' para sí o 'n' para no): ").lower()
        if opcion in ('s', 'n'):
            return opcion == 's'
        print("-----------------------------")
        print("Opción no válida. Intente nuevamente")
        print("-----------------------------")

def main():
    mostrar_portada()

    while True:
        units, simbolo = seleccionar_unidad()
        ciudad = ingresar_ciudad()
        dataClima = solicitar_clima(ciudad, API_KEY, units)
        mostrar_clima_actual(dataClima, ciudad, simbolo)

        if preguntar_pronostico():
            dataPronostico = solicitar_clima_extendido(ciudad, API_KEY, units)
            mostrar_pronostico_extendido(dataPronostico, simbolo)

        if not realizar_nueva_consulta():
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()