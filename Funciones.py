import os
import requests # type: ignore
from dotenv import load_dotenv # type: ignore


def mostrar_portada():
    print("-----------------------------")
    print("--------APP DEL CLIMA--------")
    print("by Compumundohipermegared")
    print("-----------------------------")

def seleccionar_unidad():
    while True:
        unidad = input("Unidad de temperatura (C para Celsius, F para Fahrenheit): ").strip().lower()
        if unidad == 'c':
            return 'metric', '°C'
        elif unidad == 'f':
            return 'imperial', '°F'
        else:
            print("-----------------------------")
            print("Entrada no válida. Intente nuevamente")
            print("-----------------------------")

def unidad_actual(unidad):
    if unidad == "metric":
        return"Celcius"
    elif unidad == "imperial":
        return"Fahrenheit"
    
def cambio_unidad(unidad,simbolo):
    while True:
        print("------Medidas------")
        print(f"Actual: " + unidad_actual(unidad))
        seleccion = input ("a- Celcius\nb- Fahrenheit\nc- Volver\n")
        if seleccion.lower() =="a":
            unidad ='metric', '°C'
            return unidad
        elif seleccion.lower() == "b":
            unidad = 'imperial', '°F'
            return unidad
        elif seleccion.lower() =="c":
            return unidad,simbolo
        else:
            print("---------------------------ERROR------------------------------")
            print("Opción no válida. Por favor, seleccione nuevamente a - b - c .")
            print("--------------------------------------------------------------")

    
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

def guardar_historial(ciudad, temp, minima, maxima, humedad, descripcion, simbolo):
     with open("historial_diario.txt", "a") as file:
         file.write(f"{ciudad} - Temperatura actual: {temp} {simbolo}, "
                   f"Máxima: {maxima} {simbolo}, Mínima: {minima} {simbolo}, "
                   f"Humedad: {humedad}%, Descripción: {descripcion}\n")

 
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

    guardar_historial_extendido(data_forecast, simbolo)
def guardar_historial_extendido(data_forecast, simbolo):
    """Guarda el historial del pronóstico extendido en un archivo de texto."""
    with open("historial_extendido.txt", "a") as file:  # Agregado para guardar el historial extendido
        for forecast in data_forecast['list']:
            fecha = forecast['dt_txt']
            temp_forecast = forecast['main']['temp']
            hum_forecast = forecast["main"]["humidity"]
            desc_forecast = forecast['weather'][0]['description']
            file.write(f"{fecha} - Temperatura: {temp_forecast} {simbolo}, "
                       f"Humedad: {hum_forecast}%, Descripción: {desc_forecast}\n")    

def historial():
    while True:
            print("------HISTORIAL------")
            historial = input("a- Diario\nb- Extendido\nc- Volver\n")
            if historial.lower() == "a":
                print("--Muestro historial diario--")
            elif historial.lower() =="b":
                print("--Muestro historial extendido--")
            elif historial.lower() == "c":
                break
            else:
                print("---------------------------ERROR------------------------------")
                print("Opción no válida. Por favor, seleccione nuevamente a - b - c .")
                print("--------------------------------------------------------------")

def configuracion(units,simbolo):
    while True:
            print("------CONFIGURACIÓN------")
            config = input("a- Unidad de medida\nb- Volver\n")
            if config.lower() == "a":
                units,simbolo = cambio_unidad(units,simbolo)
                return units,simbolo
            elif config.lower() == "b":
                return units,simbolo
            else: 
                print("---------------------------ERROR--------------------------")
                print("Opción no válida. Por favor, seleccione nuevamente a - b .")
                print("----------------------------------------------------------")