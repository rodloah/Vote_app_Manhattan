# backend/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Almacena los votos de cada opción
votes = {"Option A": 0, "Option B": 0}

# Datos de preferencias de los usuarios (esto es un ejemplo; se puede hacer dinámico)
users_data = {
    'User1': [5, 3, 2],  # Puntuaciones o votos en opciones específicas
    'User2': [4, 4, 4],
    'User3': [1, 5, 3],
    'TargetUser': [5, 2, 2]  # Ejemplo de usuario para calcular recomendación
}

# Función para calcular la distancia de Manhattan
def manhattan_distance(user1, user2):
    return sum(abs(a - b) for a, b in zip(user1, user2))

# Función para encontrar el vecino más cercano
def compute_nearest_neighbor(target_user, users_data):
    distances = [(user, manhattan_distance(users_data[target_user], users_data[user]))
                 for user in users_data if user != target_user]
    distances.sort(key=lambda x: x[1])  # Ordena por distancia
    return distances[0][0]  # Retorna el vecino más cercano

# Ruta para registrar el voto
@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    choice = data.get('choice')
    if choice in votes:
        votes[choice] += 1
    return jsonify(votes)

# Ruta para obtener el conteo de votos
@app.route('/votes', methods=['GET'])
def get_votes():
    return jsonify(votes)

# Ruta para calcular la recomendación basada en el vecino más cercano
@app.route('/recommend', methods=['GET'])
def recommend():
    target_user = request.args.get('user', 'TargetUser')  # Cambia 'TargetUser' según el usuario deseado
    if target_user in users_data:
        nearest_neighbor = compute_nearest_neighbor(target_user, users_data)
        return jsonify({'neighbor': nearest_neighbor})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
