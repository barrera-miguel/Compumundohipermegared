import os
import requests 
from dotenv import load_dotenv 
from datetime import datetime

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
        limpiar_consola()
        print("------Medidas------")
        print(f"Actual: " + unidad_actual(unidad))
        seleccion = input ("a- Celcius\nb- Fahrenheit\nc- Volver\n")
        if seleccion.lower() =="a":
            unidad,simbolo ='metric', '°C'
        elif seleccion.lower() == "b":
            unidad,simbolo = 'imperial', '°F'
        elif seleccion.lower() =="c":
            break
        else:
            print("---------------------------ERROR------------------------------")
            print("Opción no válida. Por favor, seleccione nuevamente a - b - c .")
            print("--------------------------------------------------------------")
    return unidad,simbolo

    
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
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guardar_historial(ciudad, temp, minima, maxima, humedad, descripcion, simbolo,fecha_actual)
        
def solicitar_clima_extendido(ciudad, API_KEY, units):
    url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={API_KEY}&units={units}&lang=es"
    res_forecast = requests.get(url_forecast)
    return res_forecast.json()

def mostrar_pronostico_extendido(data_forecast, simbolo,ciudad):
    
    print("-------Pronóstico Extendido a 5 Días-------")
    for forecast in data_forecast['list']:
        fecha = forecast['dt_txt']
        temp_forecast = forecast['main']['temp']
        hum_forecast = forecast["main"]["humidity"]
        desc_forecast = forecast['weather'][0]['description']
        print(f"{fecha}: {temp_forecast} {simbolo}, Humedad: {hum_forecast} %, {desc_forecast}")
    print("------------------------------------------")
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guardar_historial_extendido(data_forecast, simbolo,fecha_actual,ciudad)
    
def historial():
    while True:
        limpiar_consola()
        print("------HISTORIAL------")
        historial = input("a- Diario\nb- Extendido\nc- Volver\n")
        if historial.lower() == "a":
            mostrar_historial()
        elif historial.lower() =="b":
            mostrar_historial_extendido()
        elif historial.lower() == "c":
            break
        else:
            print("---------------------------ERROR------------------------------")
            print("Opción no válida. Por favor, seleccione nuevamente a - b - c .")
            print("--------------------------------------------------------------")

def guardar_historial(ciudad, temp, minima, maxima, humedad, descripcion, simbolo,fecha_actual):
    with open("historial_diario.txt", "a",encoding="utf-8") as file:
         file.write(f"----------------{ciudad}----{fecha_actual}--------------------\n"
                    f"- Temperatura actual: {temp} {simbolo}, "
                   f"Máxima: {maxima} {simbolo}, Mínima: {minima} {simbolo}, "
                   f"Humedad: {humedad}%, Descripción: {descripcion}\n"
                   f"---------------------------------------------------------------\n")

def guardar_historial_extendido(data_forecast, simbolo,fecha_actual,ciudad):
    with open("historial_extendido.txt", "a",encoding="utf-8") as file:  
        file.write(f"----------------{ciudad}------{fecha_actual}----------------\n")
        for forecast in data_forecast['list']:
            fecha = forecast['dt_txt']
            temp_forecast = forecast['main']['temp']
            hum_forecast = forecast["main"]["humidity"]
            desc_forecast = forecast['weather'][0]['description']
            file.write(f"{fecha} - Temperatura: {temp_forecast} {simbolo}, "
                       f"Humedad: {hum_forecast}%, Descripción: {desc_forecast}\n")
        file.write(f"---------------------------------------------------\n")
            
def mostrar_historial():
    while True:
        limpiar_consola()
        try:
            with open("historial_diario.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if contenido:
                    print("Historial de consultas:")
                    print(contenido)
                else:
                    print("El historial está vacío.")
        except FileNotFoundError:
            print("No se ha encontrado el archivo de historial.")
        salir = input("¿Desea salir? (SI/NO)")
        if salir.lower()=="si":
            break
        else: continue

def mostrar_historial_extendido():
    while True:
        limpiar_consola()
        try:
            with open("historial_extendido.txt", "r",encoding="utf-8") as archivo:
                contenido = archivo.read()
                if contenido:
                    print("Historial de consultas Extendido:")
                    print(contenido)
                else:
                    print("El historial está vacío.")
        except FileNotFoundError:
            print("No se ha encontrado el archivo de historial.")
        salir = input("¿Desea salir? (SI/NO)")
        if salir.lower()=="si":
            break
        else: continue


def configuracion(units,simbolo):
    while True:
        limpiar_consola()
        print("------CONFIGURACIÓN------")
        config = input("a- Unidad de medida\nb- Borrar historial Diario\nc- Borrar historial Extendido\nd- Volver\n")
        if config.lower() == "a":
            units,simbolo = cambio_unidad(units,simbolo)
        elif config.lower() == "b":
            limpiar_consola()
            seguro = input("Esta seguro de borrar el historial? (SI/NO)")
            if seguro.lower() == "si":
                with open("historial_diario.txt", "w") as archivo:
                    pass

        elif config.lower() == "c":
            limpiar_consola()
            seguro = input("Esta seguro de borrar el historial extendido? (SI/NO)")
            if seguro.lower() == "si":
                with open("historial_extendido.txt", "w") as archivo:
                    pass
        elif config.lower() == "d":
            break
        else: 
            print("---------------------------ERROR--------------------------")
            print("Opción no válida. Por favor, seleccione nuevamente a - b .")
            print("----------------------------------------------------------")
    return units,simbolo

def limpiar_consola():
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')