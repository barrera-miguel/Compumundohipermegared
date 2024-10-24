import requests

print("-----------------------------")
print("--------APP DEL CLIMA--------")
print("by Compumundohipermegared")
print("-----------------------------")

while True:
    unidad = input("Elige la unidad (C para Celsius, F para Fahrenheit): ").strip().upper()
    if unidad == 'F':
        unidades = "Imperial"  
    else:
        unidades = "Metrica"
        
        
    while True:
        ciudad = input("Ingrese una ciudad: ").title()
        if ciudad.isdigit() or len(ciudad) == 0:
            print("-----------------------------")
            print("Entrada no válida. Intente nuevamente")
            print("-----------------------------")
        else:
            break
    
    API_KEY = "928118c4d4d0be4d4e9efac728745aef"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    res = requests.get(url)
    data = res.json()

    temp = data["main"]["temp"]
    descripcion = data["weather"] [0] ["description"]
    minima = data["main"]["temp_min"]
    maxima = data["main"]["temp_max"]
    humedad = data["main"]["humidity"]

    print("-----------------------------")
    
    if unidades == "Imperial":
        temp_actual_c = (temp * 9/5) + 32
        temp_maxima_c = (maxima * 9/5) + 32
        temp_minima_c = (minima * 9/5) + 32
        print(f'Temperatura actual en {ciudad}: {temp_actual_c:.2f} °F')
        print(f'Temperatura máxima: {temp_maxima_c:.2f} °F')
        print(f'Temperatura mínima: {temp_minima_c:.2f} °F')
    else:
        print(f'Temperatura actual en {ciudad}: {temp:.2f} °C')
        print(f'Temperatura máxima: {maxima:.2f} °C')
        print(f'Temperatura mínima: {minima:.2f} °C')
    print(f"Humedad: {humedad} %")
    print(f"Descripción: {descripcion}")
    print("-----------------------------")

    while True:
        opcion_pronostico = input("¿Quiere ver el pronóstico extendido a 5 días? (ingrese 's' para sí o 'n' para no): ").lower()
        print("-----------------------------")

        if opcion_pronostico == 'n':
            break
        elif opcion_pronostico == 's':
            url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
            res_forecast = requests.get(url_forecast)
            data_forecast = res_forecast.json()

            print("-------Pronóstico Extendido a 5 Días-------")
            for forecast in data_forecast['list']:
                fecha = forecast['dt_txt']
                temp_forecast = forecast['main']['temp']
                desc_forecast = forecast['weather'][0]['description']
                if unidades == "Imperial":
                    temp_forecast_c = (temp * 9/5) + 32 
                    print(f"{fecha}: {temp_forecast_c}°F, {desc_forecast}")
                else:
                    print(f"{fecha}: {temp_forecast}°C, {desc_forecast}")
            print("------------------------------------------")
            break
        else:
            print("Opción no válida. Intente nuevamente")
            print("-----------------------------")

    while True:
        opcion = input("¿Quiere hacer otra consulta? (ingrese 's' para sí o 'n' para no): ").lower()
        print("-----------------------------")

        if opcion == 'n':
            print("Saliendo...")
            exit()
        elif opcion == 's':
            break
        else:
            print("Opción no válida. Intente nuevamente")
            print("-----------------------------")