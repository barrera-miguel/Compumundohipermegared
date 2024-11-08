from dotenv import load_dotenv
from Funciones import limpiar_consola, barra_progreso, mostrar_portada, mostrar_menu_es, mostrar_menu_en, seleccionar_language,seleccionar_unidad,ingresar_ciudad,solicitar_clima,mostrar_clima_actual,solicitar_clima_extendido,mostrar_pronostico_extendido,historial,configuracion
from rich.prompt import Prompt
import os

from idiomas import idioma

load_dotenv()

API_KEY = os.getenv("API_KEY")

limpiar_consola()
barra_progreso()
mostrar_portada()
language_code = seleccionar_language()
texts = idioma(language_code)
limpiar_consola()
units, simbolo = seleccionar_unidad(texts)

while True:
    
    limpiar_consola()
    if language_code == "es":
        mostrar_menu_es()
    else:
        mostrar_menu_en()
    # print(texts["menu"])
    seleccion = Prompt.ask(texts["seleccion_1_5"])

    if seleccion == "1":
        limpiar_consola()
        salir="yes"
        while salir !="no":
            
            ciudad = ingresar_ciudad(texts)
            mostrar_clima_actual(solicitar_clima(ciudad, API_KEY, units,language_code), ciudad, simbolo,texts)
            while True:
                salir = input(texts["otra_consulta"])
                if salir.lower()=="no":
                    break
                elif salir.lower()=="yes" or salir.lower()=="si" :
                    limpiar_consola()
                    break
                else: 
                    print(texts["entrada_no_validad"])
                    continue

    elif seleccion == "2":
        limpiar_consola()
        salir_extendido="yes"
        while salir_extendido != "no":
            ciudad = ingresar_ciudad(texts)
            mostrar_pronostico_extendido(solicitar_clima_extendido(ciudad, API_KEY, units,language_code), simbolo,ciudad,texts)
            while True:
                salir_extendido = input(texts["otra_consulta"])
                if salir_extendido.lower()=="no":
                    break
                elif salir_extendido.lower()=="yes" or salir_extendido.lower()=="si":
                    limpiar_consola()
                    break
                else: 
                    print(texts["entrada_no_validad"])
                    continue
        

    elif seleccion == "3":
        historial(texts)

    elif seleccion == "4":
       resultado = configuracion(units,simbolo,texts,language_code)
       units,simbolo= resultado["unidades"]
       language_code= resultado["lenguaje"]
       texts = idioma(language_code)


    elif seleccion == "5":
        limpiar_consola()
        continuar = input(texts["seguro_salir"])
        if continuar.lower() != 'no':
            print(texts["saliendo"])
            break
        else:print(texts["regresar_menu"])

    else:
        print("---------------------------ERROR-------------------------------")
        print(texts["opcion_no"])
        print("---------------------------------------------------------------")
           

