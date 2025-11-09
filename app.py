from flask import Flask, jsonify, request

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

# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)