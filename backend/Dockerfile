# backend/Dockerfile
FROM python:3.9

WORKDIR /app

# Actualiza pip
RUN python -m pip install --upgrade pip

# Instala Flask
RUN pip install flask

COPY . /app

CMD ["python", "app.py"]

