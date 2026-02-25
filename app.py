from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.get("/")
def index():
    return "Hola, mundo"

@app.get("/frotar/<int:n_frases>")
def frotar_endpoint(n_frases: int):
    return jsonify(frotar(n_frases))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
