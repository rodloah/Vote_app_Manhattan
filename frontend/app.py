# frontend/app.py
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# Ruta de la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar votos
@app.route('/vote', methods=['POST'])
def vote():
    choice = request.form['choice']
    # Llama al backend para registrar el voto (ajusta la URL si usas un servicio diferente)
    requests.post('http://backend:5001/vote', json={'choice': choice})
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
