from flask import Flask, jsonify, request
from flask_cors import CORS
from osm.funcion_web import ruteo

app = Flask(__name__)
CORS(app)

@app.route('/route', methods=['POST'])
def route():
    body = request.get_json()
    print(body)
    start = body['start']
    end = body['end']
    for p in [start, end]:
        assert type(p) == list
        assert len(p) == 2

    path = ruteo(start, end)
    print('Path:', path)
    return jsonify(
        path=path
    )
