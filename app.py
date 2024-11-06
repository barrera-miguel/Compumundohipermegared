from dotenv import load_dotenv
from Funciones import limpiar_consola, mostrar_portada,seleccionar_unidad,ingresar_ciudad,solicitar_clima,mostrar_clima_actual,solicitar_clima_extendido,mostrar_pronostico_extendido,historial,configuracion
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")
mostrar_portada()
units, simbolo = seleccionar_unidad()
while True:
    print("-----------MENÚ-----------\n 1- Pronóstico actual \n 2- Pronóstico extendido \n 3- Historial de consultas\n 4- Configuración \n 5- Salir ")
    seleccion = input("Seleccione una opción (1-5): ")
    if seleccion == "1":
       ciudad = ingresar_ciudad()
       mostrar_clima_actual(solicitar_clima(ciudad, API_KEY, units), ciudad, simbolo)
    elif seleccion == "2":
        ciudad = ingresar_ciudad()
        mostrar_pronostico_extendido(solicitar_clima_extendido(ciudad, API_KEY, units), simbolo,ciudad)
    elif seleccion == "3":
        historial()
    elif seleccion == "4":
       units,simbolo= configuracion(units,simbolo)
    elif seleccion == "5":
        continuar = input("¿Está seguro de querer salir? (s/n): ")
        if continuar.lower() != 'n':
            print("Saliendo...")
            break
        else:print("Regresando al menú...")
    else:
        print("---------------------------ERROR-------------------------------")
        print("Opción no válida. Por favor, seleccione nuevamente entre 1 y 5.")
        print("---------------------------------------------------------------")
           

