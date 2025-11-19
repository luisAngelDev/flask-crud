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


# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)

    