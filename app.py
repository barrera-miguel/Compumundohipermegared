from dotenv import load_dotenv
from Funciones import limpiar_consola, mostrar_portada,seleccionar_unidad,ingresar_ciudad,solicitar_clima,mostrar_clima_actual,solicitar_clima_extendido,mostrar_pronostico_extendido,historial,configuracion

import os

from idiomas import idioma

load_dotenv()

API_KEY = os.getenv("API_KEY")

mostrar_portada()
language_code = input("es = Español ------ en = English :")
texts = idioma(language_code)
units, simbolo = seleccionar_unidad(texts)

while True:
    
    limpiar_consola()
    print(texts["menu"])
    seleccion = input(texts["seleccion_1_5"])

    if seleccion == "1":
        while True:
            limpiar_consola()
            ciudad = ingresar_ciudad(texts)
            mostrar_clima_actual(solicitar_clima(ciudad, API_KEY, units,language_code), ciudad, simbolo)
            salir = input(texts["otra_consulta"])
            if salir.lower()=="no":
                break
            else: continue

    elif seleccion == "2":
        while True:
            limpiar_consola()
            ciudad = ingresar_ciudad(texts)
            mostrar_pronostico_extendido(solicitar_clima_extendido(ciudad, API_KEY, units), simbolo,ciudad,texts)
            salir_extendido = input(texts["otra_consulta"])
            if salir_extendido.lower()=="no":
                break
            else: continue

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
        if continuar.lower() != 'n':
            print(texts["saliendo"])
            break
        else:print(texts["regresar_menu"])

    else:
        print("---------------------------ERROR-------------------------------")
        print(texts["opcion_no"])
        print("---------------------------------------------------------------")
           

