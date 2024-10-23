import requests

print("-----------------------------")
print("--------APP DEL CLIMA--------")
print("by Compumundohipermegared")
print("-----------------------------")

while True:

    while True:
        ciudad = input("Ingrese una ciudad: ").title()
        if ciudad.isdigit() or len(ciudad) == 0:
            print("-----------------------------")
            print("Entrada no válida. Intente nuevamente")
            print("-----------------------------")
        else:
            break
    
    API_KEY = "a44420d695aa26daccb827e71f32aaa5"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    res = requests.get(url)
    data = res.json()

    temp = data["main"]["temp"]
    descripcion = data["weather"] [0] ["description"]
    minima = data["main"]["temp_min"]
    maxima = data["main"]["temp_max"]
    humedad = data["main"]["humidity"]

    print("-----------------------------")
    print(f"Clima en {ciudad}:")
    print(f"Temperatura actual: {temp}°")
    print(f"Temperatura mínima: {minima}°")
    print(f"Temperatura máxima: {maxima}°")
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