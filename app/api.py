from flask import Flask, jsonify, request
from app.reservations import check_availability

app = Flask(__name__)
reservations = []

@app.route('/reservations', methods=["POST"])
def create_reservation():
    data = request.get_json()
    is_available = check_availability(reservations, data)

    if is_available:
        reservations.append(data)
        return jsonify({"message":"Success"}), 201
    else:
        return jsonify({"message":"Room not available"}), 409