from flask import Flask, jsonify, request
from bayeta import frotar, insertar

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.get("/")
def index():
    return "Hola, mundo"

@app.get("/frotar/<int:n_frases>")
def frotar_endpoint(n_frases: int):
    return jsonify(frotar(n_frases))

@app.post("/frotar/add")
def add_endpoint():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "JSON inválido"}), 400

    frases = payload.get("frases")
    if not isinstance(frases, list):
        return jsonify({"error": "Se espera un JSON con clave 'frases' y una lista de strings"}), 400

    insertadas = insertar(frases)
    return jsonify({"insertadas": insertadas}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
