from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

estado_motor = "desconocido"
ultima_temperatura = None
ultima_id = None

@app.route("/estado", methods=["GET"])
def get_estado():
    return estado_motor

@app.route("/activar", methods=["POST"])
def activar_motor():
    global estado_motor
    estado_motor = "✅ ENCENDIDO"
    return "Motor activado"

@app.route("/desactivar", methods=["POST"])
def desactivar_motor():
    global estado_motor
    estado_motor = "⛔ APAGADO"
    return "Motor desactivado"

@app.route("/temperatura", methods=["GET", "POST"])
def temperatura():
    global ultima_temperatura, ultima_id
    if request.method == "POST":
        valor = request.args.get("valor")
        id_envio = request.args.get("id")
        if valor:
            ultima_temperatura = valor
            ultima_id = id_envio or str(time.time())
            return f"Temperatura recibida: {valor} con ID {ultima_id}"
        return "Falta el parámetro 'valor'", 400
    else:
        return jsonify({
            "ultima": ultima_temperatura or "No disponible",
            "id": ultima_id or "0"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
