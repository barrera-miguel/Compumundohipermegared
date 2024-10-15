#App del clima by Compumundohipermegared

##Indice
1- Manual de instalación y deployment 
2- Funcionamiento del App
3- Tecnologías empleadas
4- Roadmap

## 1-Manual de instalación y deployment 

-a- Ubicarse en el directorio deseado
-b- Iniciar terminal y ejecutar comandos.
-c- Clonar el repositorio:
git clone https://github.com/barrera-miguel/Compumundohipermegared.git
-d- Construye la imagen de Docker
docker build -t nombre_imagen 
-e- Ejecuta el contenedor
docker run -it --rm nombre_imagen 

## 2-Funcionamiento del App

Aplicación interactiva que permite a los usuarios
consultar el estado del clima actual de cualquier ciudad, utilizando una API
externa para obtener los datos meteorológicos. La aplicación esta
diseñada en Python, implementada en contenedores Docker, y aplica la
metodología Scrum para su desarrollo en equipo. Proporciona un
menú interactivo en consola para realizar múltiples consultas y
ofrecer diversas funcionalidades adicionales, como la posibilidad de cambiar
unidades de medida, guardar un historial de consultas y mostrar el pronóstico
del clima para los próximos días.

## 3-Tecnologías empleadas
- Phyton

## 4-Roadmap
HU1: Consultar el Clima Actual de una Ciudad
HU2: Cambiar las Unidades de Temperatura
HU3: Consultar el Pronóstico del Clima
HU4: Ver Historial de Consultas
HU5: Notificación de Error en la Consulta




