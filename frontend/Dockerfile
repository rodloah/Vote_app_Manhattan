# frontend/Dockerfile
FROM python:3.9

WORKDIR /app

# Instala Flask y Requests
RUN pip install flask requests

COPY . /app

CMD ["python", "app.py"]

