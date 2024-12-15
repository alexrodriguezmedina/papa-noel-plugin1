from flask import Flask, request, jsonify

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def home():
    return "Benvingut a l'API de Papà Noel! Visita /papa_noel per parlar amb ell."

# Definir el endpoint /papa_noel
@app.route('/papa_noel', methods=['POST'])
def respond():
    # Leer la pregunta que envía el usuario
    data = request.json
    pregunta = data.get('pregunta', '').lower()

    # Responder según las palabras clave
    if "regal" in pregunta:
        resposta = "Ho ho ho! Els regals són màgics! Estic revisant la teva llista!"
    elif "nadal" in pregunta:
        resposta = "El Nadal és un moment per compartir alegria i amor amb els teus éssers estimats!"
    else:
        resposta = "Ho ho ho! Sóc Papà Noel. Com puc ajudar-te avui?"

    # Enviar la respuesta
    return jsonify({"resposta": resposta})

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)