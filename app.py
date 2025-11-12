from flask import Flask, jsonify, request
import json
import os

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta inicial (home)
@app.route('/')
def home():
    return jsonify({
        "message": "Bienvenido a mi API CRUD con Flask",
        "status": "running"
    })


# Ejemplo de endpoint tipo GET
@app.route('/saludo/<nombre>', methods=['GET'])
def saludar(nombre):
    return jsonify({
        "saludo": f"Hola {nombre}, bienvenido a la API de Flask!"
    })

DATA_FILE = "data.json"

# Crear el archivo si no existe
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)


def leer_datos():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def guardar_datos(datos):
    with open(DATA_FILE, "w") as f:
        json.dump(datos, f, indent=4)


@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify(leer_datos())



@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    usuarios = leer_datos()
    nuevo = request.get_json()

    if not nuevo.get("nombre") or not nuevo.get("email"):
        return jsonify({"error": "Faltan campos"}), 400

    nuevo["id"] = max([u["id"] for u in usuarios], default=0) + 1
    usuarios.append(nuevo)
    guardar_datos(usuarios)

    return jsonify(nuevo), 201




# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)