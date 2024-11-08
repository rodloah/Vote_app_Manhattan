# backend/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

votes = {"Option A": 0, "Option B": 0}

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    choice = data.get('choice')
    if choice in votes:
        votes[choice] += 1
    return jsonify(votes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

