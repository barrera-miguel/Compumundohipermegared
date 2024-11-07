import os
import requests 
from dotenv import load_dotenv 
from datetime import datetime
from idiomas import idioma


def mostrar_portada():
    print("-----------------------------")
    print("--------APP DEL CLIMA--------")
    print("by Compumundohipermegared")
    print("-----------------------------")

def seleccionar_language():
    while True:
        print("")
        lenguaje  = input("Español = es / English = en : ")
        if lenguaje.lower() == "es":
            return "es"
        elif lenguaje.lower() == "en":
            return "en"
        else:
            print("-------------------------------------")
            print("Caracter invalido / Invalid character")
            print("-------------------------------------")
    

def seleccionar_unidad(texts):
    while True:
        unidad = input(texts['selec_unidad']).strip().lower()
        if unidad.lower() == 'c':
            return 'metric', '°C'
        elif unidad.lower() == 'f':
            return 'imperial', '°F'
        else:
            print("-----------------------------")
            print(texts["entrada_no_validad"])
            print("-----------------------------")

def unidad_actual(unidad):
    if unidad == "metric":
        return"Celcius"
    elif unidad == "imperial":
        return"Fahrenheit"
    
def cambio_unidad(unidad,simbolo,texts):
    while True:
        limpiar_consola()
        print(texts["medidas"])
        print(texts["actual"] + unidad_actual(unidad))
        seleccion = input (texts["opciones_medidas"])
        if seleccion.lower() =="a":
            unidad,simbolo ='metric', '°C'
        elif seleccion.lower() == "b":
            unidad,simbolo = 'imperial', '°F'
        elif seleccion.lower() =="c":
            break
        else:
            print("---------------------------ERROR------------------------------")
            print(texts["error_medidas"])
            print("--------------------------------------------------------------")
    return unidad,simbolo

    
def ingresar_ciudad(texts):
    while True:
        ciudad = input(texts["ingrese_ciudad"]).strip().title()
        if ciudad.isdigit() or len(ciudad) == 0:
            print("-----------------------------")
            print(texts["error_ciudad"])
            print("-----------------------------")
        else:
            return ciudad

def solicitar_clima(ciudad, API_KEY, units,lenguaje):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units={units}&lang={lenguaje}"
    res = requests.get(url)
    return res.json()

def mostrar_clima_actual(data, ciudad, simbolo,texts):
    temp = data["main"]["temp"]
    descripcion = data["weather"] [0] ["description"]
    minima = data["main"]["temp_min"]
    maxima = data["main"]["temp_max"]
    humedad = data["main"]["humidity"]
    print("-----------------------------")
    print(texts["temp_actual"] + f"{ciudad}: {temp} {simbolo}")
    print(texts["temp_maxima"] + f"{maxima} {simbolo}")
    print(texts["temp_minima"]+f"{minima} {simbolo}")
    print(texts["humedad"]+f"{humedad} %")
    print(texts["descripcion"]+f"{descripcion}")
    print("-----------------------------")
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guardar_historial(ciudad, temp, minima, maxima, humedad, descripcion, simbolo,fecha_actual,texts)
        
def solicitar_clima_extendido(ciudad, API_KEY, units,lenguaje):
    url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={API_KEY}&units={units}&lang={lenguaje}"
    res_forecast = requests.get(url_forecast)
    return res_forecast.json()

def mostrar_pronostico_extendido(data_forecast, simbolo,ciudad,texts):
    
    print(texts["pronostico_5"])
    for forecast in data_forecast['list']:
        fecha = forecast['dt_txt']
        temp_forecast = forecast['main']['temp']
        hum_forecast = forecast["main"]["humidity"]
        desc_forecast = forecast['weather'][0]['description']
        print((f"{fecha}: {temp_forecast} {simbolo} ")+ texts["humedad"] + (f"{hum_forecast} %, {desc_forecast}"))
    print("------------------------------------------")
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guardar_historial_extendido(data_forecast, simbolo,fecha_actual,ciudad,texts)
    
def historial(texts):
    while True:
        limpiar_consola()
        print(texts["historial"])
        historial = input(texts["opciones_historial"])
        if historial.lower() == "a":
            mostrar_historial(texts)
        elif historial.lower() =="b":
            mostrar_historial_extendido(texts)
        elif historial.lower() == "c":
            break
        else:
            print("---------------------------ERROR------------------------------")
            print(texts["error_historial"])
            print("--------------------------------------------------------------")

def guardar_historial(ciudad, temp, minima, maxima, humedad, descripcion, simbolo,fecha_actual,texts):
    with open("historial_diario.txt", "a",encoding="utf-8") as file:
         file.write(f"----------------{ciudad}----{fecha_actual}--------------------\n"
                     f"{texts["temp_actual"]} {temp} {simbolo}, "
                   f"{texts["temp_maxima"]} {maxima} {simbolo}, {texts["temp_minima"]} {minima} {simbolo}, "
                   f"{texts["humedad"]}{humedad}%, {texts["descripcion"]} {descripcion}\n"
                   f"---------------------------------------------------------------\n")

def guardar_historial_extendido(data_forecast, simbolo,fecha_actual,ciudad,texts):
    with open("historial_extendido.txt", "a",encoding="utf-8") as file:  
        file.write(f"----------------{ciudad}------{fecha_actual}----------------\n")
        for forecast in data_forecast['list']:
            fecha = forecast['dt_txt']
            temp_forecast = forecast['main']['temp']
            hum_forecast = forecast["main"]["humidity"]
            desc_forecast = forecast['weather'][0]['description']
            file.write(f"{fecha} {texts["temp_extendido"]} {temp_forecast} {simbolo}, "
                       f"{texts["humedad"]}{hum_forecast}%, {texts["descripcion"]} {desc_forecast}\n")
        file.write(f"---------------------------------------------------\n")
            
def mostrar_historial(texts):
    while True:
        limpiar_consola()
        try:
            with open("historial_diario.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if contenido:
                    print(texts["historial_consultas"])
                    print(contenido)
                else:
                    print(texts["archivo_vacio"])
        except FileNotFoundError:
            print(texts["no_archivo"])
        salir = input(texts["desea_salir"])
        if salir.lower() == "si" or salir.lower() == "yes":
            break
        else: continue

def mostrar_historial_extendido(texts):
    while True:
        limpiar_consola()
        try:
            with open("historial_extendido.txt", "r",encoding="utf-8") as archivo:
                contenido = archivo.read()
                if contenido:
                    print(texts["historial_consultas_extendido"])
                    print(contenido)
                else:
                    print(texts["archivo_vacio"])
        except FileNotFoundError:
            print(texts["no_archivo"])
        salir = input(texts["desea_salir"])
        if salir.lower() == "si" or salir.lower() == "yes":
            break
        else: continue


def configuracion(units,simbolo,texts,language_code):
    while True:
        limpiar_consola()
        print(texts["configuracion"])
        config = input(texts["opciones_configuracion"])
        if config.lower() == "a":
            units,simbolo = cambio_unidad(units,simbolo,texts)
        elif config.lower() == "b":
            limpiar_consola()
            print(texts["idiomas"])
            idioma = input(texts["opciones_idiomas"]+"\n")
            if idioma == "a":
                language_code ="es"
                break
            elif idioma == "b":
                language_code = "en"
                break
            else:print(texts["error_ciudad"])
           
        elif config.lower() == "c":
            limpiar_consola()
            seguro = input(texts["seguro_historial"])
            if seguro.lower() == "si" or  seguro.lower() == "yes":
                with open("historial_diario.txt", "w") as archivo:
                    pass
        elif config.lower() == "d":
            limpiar_consola()
            seguro = input(texts["seguro_extendido"])
            if seguro.lower() == "si" or  seguro.lower() == "yes":
                with open("historial_extendido.txt", "w") as archivo:
                    pass
        elif config.lower() == "e":
            break
        else: 
            print("---------------------------ERROR--------------------------")
            print(texts["error_configuracion"])
            print("----------------------------------------------------------")
    return {"unidades":(units,simbolo),"lenguaje":language_code}

def limpiar_consola():
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')