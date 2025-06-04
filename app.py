from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

estado_motor = "desconocido"
ultima_temperatura = None

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
    global ultima_temperatura
    if request.method == "POST":
        valor = request.args.get("valor")
        if valor:
            ultima_temperatura = valor
            return f"Temperatura recibida: {valor}°C"
        return "Falta el parámetro 'valor'", 400
    else:
        return jsonify({"ultima": ultima_temperatura or "No disponible"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
