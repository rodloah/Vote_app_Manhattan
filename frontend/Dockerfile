# frontend/Dockerfile
FROM python:3.9

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install flask requests

COPY . /app

CMD ["python", "app.py"]
