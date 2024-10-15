import requests

print("-----------------------------")
print("--------APP DEL CLIMA--------")
print("by Compumundohipermegared")
print("-----------------------------")
print("Para consultar la temperatura complete los siguientes datos")
departamento= input("Ingrese la ciudad: ")

provincia = input("Ingrese la provincia: ")

pais = "AR"

api_key ="0f331f0efeb776ca406e32210a0cb36f"

url=f"https://api.openweathermap.org/data/2.5/weather?q={departamento},{provincia},{pais}&units=metric&appid={api_key}"

res = requests.get(url)

data = res.json()

temp = data["main"]["temp"]
descripcion= data["weather"] [0] ["description"]
minima= data["main"]["temp_min"]
maxima= data["main"]["temp_max"]
humedad= data["main"]["humidity"]
print("-----------------------------")
print("Temperatura actual: ", temp)
print("Temperatura mínima: ", minima)
print("Temperatura máxima: ", maxima)
print("Humedad:", humedad,"%")
print("Descripción: ", descripcion)
print("-----------------------------")








