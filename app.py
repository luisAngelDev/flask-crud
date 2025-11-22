from flask import Flask, jsonify, request
import json
import os

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta del archivo JSON
DATA_FILE = "pets.json"


def cargar_datos():
    """Lee los datos del archivo JSON"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_datos(data):
    """Guarda la lista completa en el archivo JSON"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.route("/")
def index():
    mascotas = cargar_datos()
    return render_template("index.html", mascotas=mascotas)


@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        mascotas = cargar_datos()

        nueva_mascota = {
            "id": (mascotas[-1]["id"] + 1) if mascotas else 1,
            "nombre": request.form["nombre"],
            "tipo": request.form["tipo"],
            "edad": int(request.form["edad"]),
            "vacunado": True if request.form.get("vacunado") == "on" else False
        }

        mascotas.append(nueva_mascota)
        guardar_datos(mascotas)

        return redirect(url_for("index"))

    return render_template("add_pet.html")


@app.route("/eliminar/<int:pet_id>")
def eliminar(pet_id):
    mascotas = cargar_datos()
    mascotas = [m for m in mascotas if m["id"] != pet_id]
    guardar_datos(mascotas)
    return redirect(url_for("index"))



@app.route("/api/pets")
def api_get_pets():
    return jsonify(cargar_datos())


@app.route("/api/pets/<int:pet_id>")
def api_get_pet(pet_id):
    mascotas = cargar_datos()
    pet = next((m for m in mascotas if m["id"] == pet_id), None)
    return jsonify(pet if pet else {"error": "No encontrado"})


@app.route("/api/pets", methods=["POST"])
def api_create_pet():
    mascotas = cargar_datos()
    data = request.json

    nueva = {
        "id": (mascotas[-1]["id"] + 1) if mascotas else 1,
        "nombre": data["nombre"],
        "tipo": data["tipo"],
        "edad": data["edad"],
        "vacunado": data["vacunado"]
    }

    mascotas.append(nueva)
    guardar_datos(mascotas)

    return jsonify(nueva), 201



@app.route("/api/pets", methods=["POST"])
def api_create_pet():
    mascotas = cargar_datos()
    data = request.json

    nueva = {
        "id": (mascotas[-1]["id"] + 1) if mascotas else 1,
        "nombre": data["nombre"],
        "tipo": data["tipo"],
        "edad": data["edad"],
        "vacunado": data["vacunado"]
    }

    mascotas.append(nueva)
    guardar_datos(mascotas)

    return jsonify(nueva), 201


@app.route("/api/pets/<int:pet_id>", methods=["PUT"])
def api_update_pet(pet_id):
    mascotas = cargar_datos()
    data = request.json

    for m in mascotas:
        if m["id"] == pet_id:
            m["nombre"] = data.get("nombre", m["nombre"])
            m["tipo"] = data.get("tipo", m["tipo"])
            m["edad"] = data.get("edad", m["edad"])
            m["vacunado"] = data.get("vacunado", m["vacunado"])
            guardar_datos(mascotas)
            return jsonify(m)

    return jsonify({"error": "No encontrado"}), 404

# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)

    