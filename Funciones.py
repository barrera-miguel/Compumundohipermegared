import os
import requests # type: ignore
from dotenv import load_dotenv # type: ignore
from datetime import datetime
from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.box import HEAVY

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

def mostrar_menu():
    table = Table(show_header=False, box=HEAVY, show_lines=True)
    
    table.add_row("[bold yellow]1[/bold yellow]", "[yellow]Pronóstico actual[/yellow]")
    table.add_row("[bold green]2[/bold green]", "[green]Pronóstico extendido[/green]")
    table.add_row("[bold blue]3[/bold blue]", "[blue]Historial de consultas[/blue]")
    table.add_row("[bold magenta]4[/bold magenta]", "[magenta]Configuración[/magenta]")
    table.add_row("[bold red]5[/bold red]", "[red]Salir[/red]")

    panel = Panel(table, title="MENÚ", title_align="center", border_style="cyan", expand=False)

    print(panel)

def seleccionar_unidad():
    while True:
        # Solicitar la unidad de temperatura usando Rich para darle estilo al prompt
        unidad = Prompt.ask(
            "[bold cyan]Unidad de temperatura[/bold cyan] ([bold yellow]C[/bold yellow] para [bold yellow]Celsius[/bold yellow], [bold green]F[/bold green] para [bold green]Fahrenheit[/bold green])"
        ).strip().lower()

        if unidad == 'c':
            return 'metric', '°C'
        elif unidad == 'f':
            return 'imperial', '°F'
        else:
            # Mensaje de error estilizado
            error_panel = Panel(
                "[bold red]⚠️  Entrada no válida. Intente nuevamente.[/bold red]",
                border_style="red",
                expand=False
            )
            print(error_panel)

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
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guardar_historial(ciudad, temp, minima, maxima, humedad, descripcion, simbolo,fecha_actual)
 
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
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    guardar_historial_extendido(data_forecast, simbolo,fecha_actual)
   

def historial():
    while True:
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
     with open("historial_diario.txt", "a") as file:
         file.write(f"----------------{ciudad}----{fecha_actual}--------------------\n"
                    f"- Temperatura actual: {temp} {simbolo}, "
                   f"Máxima: {maxima} {simbolo}, Mínima: {minima} {simbolo}, "
                   f"Humedad: {humedad}%, Descripción: {descripcion}\n"
                   f"---------------------------------------------------------------\n")

def guardar_historial_extendido(data_forecast, simbolo,fecha_actual):
    """Guarda el historial del pronóstico extendido en un archivo de texto."""
    with open("historial_extendido.txt", "a") as file:  # Agregado para guardar el historial extendido
        file.write(f"----------------{fecha_actual}----------------\n")
        for forecast in data_forecast['list']:
            fecha = forecast['dt_txt']
            temp_forecast = forecast['main']['temp']
            hum_forecast = forecast["main"]["humidity"]
            desc_forecast = forecast['weather'][0]['description']
            file.write(f"{fecha} - Temperatura: {temp_forecast} {simbolo}, "
                       f"Humedad: {hum_forecast}%, Descripción: {desc_forecast}\n")
        file.write(f"---------------------------------------------------\n")
            
def mostrar_historial():
    try:
        with open("historial_diario.txt", "r", encoding="latin-1") as archivo:
            contenido = archivo.read()
            if contenido:
                print("Historial de consultas:")
                print(contenido)
            else:
                print("El historial está vacío.")
    except FileNotFoundError:
        print("No se ha encontrado el archivo de historial.")

def mostrar_historial_extendido():
    try:
        with open("historial_extendido.txt", "r",encoding="latin-1") as archivo:
            contenido = archivo.read()
            if contenido:
                print("Historial de consultas Extendido:")
                print(contenido)
            else:
                print("El historial está vacío.")
    except FileNotFoundError:
        print("No se ha encontrado el archivo de historial.")


def configuracion(units,simbolo):
    while True:
            print("------CONFIGURACIÓN------")
            config = input("a- Unidad de medida\nb- Borrar historial Diario\nc- Borrar historial Extendido\nd- Volver\n")
            if config.lower() == "a":
                units,simbolo = cambio_unidad(units,simbolo)
                return units,simbolo
            elif config.lower() == "b":
                with open("historial_diario.txt", "w") as archivo:
                    pass
                print("Historial diario borrado correctamente.")
            elif config.lower() == "c":
                with open("historial_extendido.txt", "w") as archivo:
                    pass
                print("Historial extendido borrado correctamente.")
            elif config.lower() == "d":
                return units,simbolo
            else: 
                print("---------------------------ERROR--------------------------")
                print("Opción no válida. Por favor, seleccione nuevamente a - b .")
                print("----------------------------------------------------------")