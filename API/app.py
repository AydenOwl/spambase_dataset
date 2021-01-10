from flask import Flask, render_template, request
from flask_cors import CORS
import json
from joblib import load

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    # Récupération du tableau
    pred = request.get_json()
    # Erreur si taille différent de 57 pour le tableau
    status = 400
    res = 'Erreur: le tableau doit être de taile 57.'

    if len(pred) == 57:
        # Chargement du modèle
        model = load('spam_classificator.joblib')
        # Création de la requête
        res = 'spam'
        if model.predict([pred])[0] == 0:
            res = 'mail'
        status = 200

    response = app.response_class(
        response=json.dumps(res),
        status=status,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
