from flask import Flask, jsonify, request
from routes import cadastrar_time, select_time_favorito, deletar_time_favorito


app = Flask(__name__)

@app.route('/deletar/time-favorito', methods=['DELETE'])
def deletar_time():
    # nome_time = request.args['team_name']
    body = request.get_json()
    return jsonify(deletar_time_favorito(body)), 200


@app.route('/cadastrar/time-favorito', methods=['POST'])
def request_time():
    # nome_time = request.args['team_name']
    body = request.get_json()
    return jsonify(cadastrar_time(body)), 201


@app.route('/time-favorito')
def time_favorito():
    # nome_time = request.args['team_name']
    nome = request.args['nome']
    return jsonify(select_time_favorito(nome)), 200


app.run(host="0.0.0.0", port="7000", debug=True)
