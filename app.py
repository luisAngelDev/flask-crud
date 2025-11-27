from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "mensaje": "Microservicio Flask funcionando",
        "endpoints": ["/scrape", "/status"]
    })

@app.route("/status")
def status():
    return jsonify({"status": "ok"})


# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)

