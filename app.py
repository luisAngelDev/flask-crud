from flask import Flask, jsonify, request
import json
import os

# Crear la aplicación Flask
app = Flask(__name__)


# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)

    