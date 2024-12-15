from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Benvingut a l'API de Papà Noel! Visita /papa_noel per parlar amb ell."

@app.route('/papa_noel', methods=['POST'])
def respond():
    data = request.json
    pregunta = data.get('pregunta', '').lower()

    if "regal" in pregunta:
        resposta = "Ho ho ho! Els regals són màgics! Estic revisant la teva llista!"
    elif "nadal" in pregunta:
        resposta = "El Nadal és un moment per compartir alegria i amor amb els teus éssers estimats!"
    else:
        resposta = "Ho ho ho! Sóc Papà Noel. Com puc ajudar-te avui?"

    return jsonify({"resposta": resposta})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usar el puerto asignado o 5000 por defecto
    app.run(host='0.0.0.0', port=port)