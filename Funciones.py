import os
import requests 
from dotenv import load_dotenv 
from datetime import datetime
from idiomas import idioma

from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.box import HEAVY
from rich.progress import Progress
import time

def barra_progreso():
    # Crear una barra de progreso
    with Progress(transient=True) as progress:
        # Añadir una tarea a la barra de progreso
        tarea = progress.add_task("[cyan]Iniciando...", total=100)

        # Simulación de avance en la tarea
        while not progress.finished:
            # Avanzar la barra
            progress.update(tarea, advance=5)
            time.sleep(0.1)  # Simula una operación en progreso

def mostrar_portada():
    # Crear el contenido de la portada con estilo de color
    contenido_portada = "[bold cyan]APP DEL CLIMA 🔆[/bold cyan]\n[gray82]by Compumundohipermegared[/gray82]"

    # Crear un panel alrededor del contenido de la portada
    portada_panel = Panel(
        contenido_portada,
        title_align="center",
        border_style="cyan",
        padding=(1, 4),  # Añadir algo de espacio alrededor del contenido
        expand=False
    )

    # Imprimir el panel
    print(portada_panel)

def mostrar_menu_es():
    table = Table(show_header=False, box=HEAVY, show_lines=True)
    
    table.add_row("[bold yellow]1[/bold yellow]", "[yellow]Pronóstico actual[/yellow]")
    table.add_row("[bold green]2[/bold green]", "[green]Pronóstico extendido[/green]")
    table.add_row("[bold blue]3[/bold blue]", "[blue]Historial de consultas[/blue]")
    table.add_row("[bold magenta]4[/bold magenta]", "[magenta]Configuración[/magenta]")
    table.add_row("[bold red]5[/bold red]", "[red]Salir[/red]")

    panel = Panel(table, title="MENÚ", title_align="center", border_style="cyan", expand=False)

    print(panel)

def mostrar_menu_en():
    table = Table(show_header=False, box=HEAVY, show_lines=True)
    
    table.add_row("[bold yellow]1[/bold yellow]", "[yellow]Current forecast[/yellow]")
    table.add_row("[bold green]2[/bold green]", "[green]Extended forecast[/green]")
    table.add_row("[bold blue]3[/bold blue]", "[blue]Query history[/blue]")
    table.add_row("[bold magenta]4[/bold magenta]", "[magenta]Settings[/magenta]")
    table.add_row("[bold red]5[/bold red]", "[red]Exit[/red]")

    panel = Panel(table, title="MENU", title_align="center", border_style="cyan", expand=False)

    print(panel)    

def seleccionar_language():
    while True:
        print()  # Espacio en blanco para separar los mensajes

        # Solicitar el idioma al usuario con un mensaje estilizado
        print("[cyan]Selecciona el idioma / Select language[/cyan]")
        lenguaje = Prompt.ask("[cyan]Español = [bold magenta]es[/bold magenta] / English = [bold magenta]en[/bold magenta]").strip().lower()
        if lenguaje == "es":
            return "es"
        elif lenguaje == "en":
            return "en"
        else:
            # Mensaje de error en un panel estilizado
            error_panel = Panel(
                "[bold red]⚠️  Entrada no válida / Invalid input[/bold red]",
                border_style="red",
                expand=False
            )
            limpiar_consola()
            print(error_panel)
    

def seleccionar_unidad(texts):
    while True:
        print()
        unidad = Prompt.ask(texts['selec_unidad']).strip().lower()
        if unidad == 'c':
            return 'metric', '°C'
        elif unidad == 'f':
            return 'imperial', '°F'
        else:
            # Mensaje de error estilizado
            error_panel = Panel(
                texts['entrada_no_validad'],
                border_style="red",
                expand=False
            )
            limpiar_consola()
            print(error_panel)

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
            limpiar_consola()
            print("-----------------------------")
            print(texts["error_ciudad"])
            print("-----------------------------")
        else:
            return ciudad

def solicitar_clima(ciudad, API_KEY, units, lenguaje,texts):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units={units}&lang={lenguaje}"
    
    try:
        res = requests.get(url, timeout=10)  
        res.raise_for_status() 
        limpiar_consola()
        return res.json()
    except requests.exceptions.HTTPError as e:
        print(f"{texts['error_1']} {e} {texts['error_2']} {res.status_code}")
    except requests.exceptions.ConnectionError:
        print(texts['error_3'])
    except requests.exceptions.Timeout:
        print(texts['error_4'])
    except requests.exceptions.RequestException as e:
        print(f"{texts['error_5']}{e}")
    return None  
from datetime import datetime

def mostrar_clima_actual(data, ciudad, simbolo, texts):
    if data is None:
        print("----------------------------------------------------------------------------")
        print(f"{texts['error_6']} {ciudad}. {texts['error_7']}")
        print("----------------------------------------------------------------------------")
        return
    elif "main" not in data or "weather" not in data:
        print(f"{texts['error_8']} {ciudad}.")
        print(f"{texts['error_9']} {data.get('message', texts['error_10'])}")
        return
    
    try:
        temp = data["main"]["temp"]
        descripcion = data["weather"][0]["description"]
        minima = data["main"]["temp_min"]
        maxima = data["main"]["temp_max"]
        humedad = data["main"]["humidity"]

        print("-----------------------------")
        print(texts["temp_actual"] + f"{ciudad}: {temp} {simbolo}")
        print(texts["temp_maxima"] + f"{maxima} {simbolo}")
        print(texts["temp_minima"] + f"{minima} {simbolo}")
        print(texts["humedad"] + f"{humedad} %")
        print(texts["descripcion"] + f"{descripcion}")
        print("-----------------------------")
        
       
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
      
        guardar_historial(ciudad, temp, minima, maxima, humedad, descripcion, simbolo, fecha_actual, texts)
    
    except KeyError as e:
        print(f"{texts['error_12']} {e}.")


        
def solicitar_clima_extendido(ciudad, API_KEY, units, lenguaje,texts):
    url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={API_KEY}&units={units}&lang={lenguaje}"
    
    try:
        res_forecast = requests.get(url_forecast, timeout=10)
        res_forecast.raise_for_status()  
        return res_forecast.json()
    except requests.exceptions.HTTPError as e:
        print(f"{texts['error_1']} {e} {texts['error_2']}  {res_forecast.status_code}")
    except requests.exceptions.ConnectionError:
        print(texts['error_3'])
    except requests.exceptions.Timeout:
        print(texts['error_4'])
    except requests.exceptions.RequestException as e:
        print(f"{texts['error_5']}{e}")
    return None  

def mostrar_pronostico_extendido(data_forecast, simbolo, ciudad, texts):
    
    if data_forecast is None:
        print("---------------------------------------------------------------------------------")
        print(f"{texts['error_6']} {ciudad}. {texts['error_7']}")
        print("---------------------------------------------------------------------------------")
        return
    elif "list" not in data_forecast:
        print(f"{texts['error_11']} {ciudad}.")
        print(f"{texts['error_9']} {data.get('message', texts['error_10'])}")
        return
    
    try:
        print(texts["pronostico_5"]+f"{ciudad}-------")
        count = 0
        for forecast in data_forecast['list']:
            if count % 4 == 0:
                fecha = forecast['dt_txt']
                temp_forecast = forecast['main']['temp']
                hum_forecast = forecast["main"]["humidity"]
                desc_forecast = forecast['weather'][0]['description']
                print((f"{fecha}: {temp_forecast} {simbolo} ") + texts["humedad"] + (f"{hum_forecast} %, {desc_forecast}"))
            count += 1
        print("------------------------------------------")
        
        # Guarda en el historial
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        guardar_historial_extendido(data_forecast, simbolo, fecha_actual, ciudad, texts)
    
    except KeyError as e:
        print(f"{texts['error_12']} {e}.")

    
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

def guardar_historial(ciudad, temp, minima, maxima, humedad, descripcion, simbolo, fecha_actual, texts):
    with open("historial_diario.txt", "a", encoding="utf-8") as file:
         file.write(f"----------------{ciudad}----{fecha_actual}--------------------\n"
                    f"{texts['temp_actual']} {temp} {simbolo}, "
                    f"{texts['temp_maxima']} {maxima} {simbolo}, {texts['temp_minima']} {minima} {simbolo}, "
                    f"{texts['humedad']}{humedad}%, {texts['descripcion']} {descripcion}\n"
                    f"---------------------------------------------------------------\n")
def guardar_historial_extendido(data_forecast, simbolo, fecha_actual, ciudad, texts):
    with open("historial_extendido.txt", "a", encoding="utf-8") as file:
        file.write(f"----------------{ciudad}------{fecha_actual}----------------\n")
        count = 0
        for forecast in data_forecast['list']:
            if count % 4 == 0:  # Solo guarda cada 4 elementos
                fecha = forecast['dt_txt']
                temp_forecast = forecast['main']['temp']
                hum_forecast = forecast["main"]["humidity"]
                desc_forecast = forecast['weather'][0]['description']
                file.write(f"{fecha} {texts['temp_extendido']} {temp_forecast} {simbolo}, "
                           f"{texts['humedad']}{hum_forecast}%, {texts['descripcion']} {desc_forecast}\n")
            count += 1
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