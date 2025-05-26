from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route("/api/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    try:
        age = int(data["age"])
        weight = float(data["weight"])
        height = float(data["height"])
        gender = data["gender"].lower()

        s = 5 if gender == "male" else -161
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + s
        maintenance = bmr * 1.2
        deficit = maintenance * 0.8
        surplus = maintenance * 1.2

        return jsonify({
            "bmr": round(bmr, 2),
            "maintenance": round(maintenance, 2),
            "deficit": round(deficit, 2),
            "surplus": round(surplus, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/", methods=["GET"])
def root():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
