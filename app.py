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



# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)

    