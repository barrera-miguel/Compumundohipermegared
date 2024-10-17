# App del Clima por Compumundohipermegared

## Índice
1. [Manual de Instalación y Deployment](#manual-de-instalación-y-deployment)
2. [Funcionamiento de la App](#funcionamiento-de-la-app)
3. [Tecnologías Empleadas](#tecnologías-empleadas)
4. [Roadmap](#roadmap)

## Manual de Instalación y Deployment
1. Ubicarse en el directorio deseado.
2. Iniciar la terminal y clonar el repositorio:
     ```bash
     git clone https://github.com/barrera-miguel/Compumundohipermegared.git
     ```
3. Modificar el archivo app.py para incluir tu clave API
    - API_KEY en línea 19:
     ```bash
     API_KEY = "tu_api_key_aquí"
     ```
4. Ejecutar Docker en terminal
   - Construir la imagen de Docker:
     ```bash
     docker build -t nombre_imagen .
     ```
   - Ejecutar el contenedor:
     ```bash
     docker run -it --rm nombre_imagen
     ```

## Funcionamiento de la App
Esta aplicación interactiva permite a los usuarios consultar el estado del clima actual de cualquier ciudad, utilizando una API externa para obtener los datos meteorológicos. Está diseñada en Python, implementada en contenedores Docker y aplica la metodología Scrum para su desarrollo en equipo. Proporciona un menú interactivo en consola para realizar múltiples consultas y ofrece funcionalidades adicionales, como la posibilidad de cambiar unidades de medida, guardar un historial de consultas y mostrar el pronóstico del clima para los próximos días.

## Tecnologías Empleadas
- Python
- Docker

## Roadmap
- **HU1**: Consultar el Clima Actual de una Ciudad
- **HU2**: Cambiar las Unidades de Temperatura
- **HU3**: Consultar el Pronóstico del Clima
- **HU4**: Ver Historial de Consultas
- **HU5**: Notificación de Error en la Consulta



