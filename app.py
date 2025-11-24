from flask import Flask, jsonify, request
import json
import os

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta del archivo JSON
DATA_FILE = "pets.json"


# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)

