FROM python:3.9-slim 

WORKDIR /app 

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

COPY . . 
COPY requirements.txt .
COPY historial_diario.txt .
COPY historial_extendido.txt .

RUN pip install --no-cache-dir -r requirements.txt 

CMD ["python", "app.py"]