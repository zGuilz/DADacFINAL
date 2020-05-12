from flask import Flask, jsonify, request
from routes import get_team


app = Flask(__name__)

@app.route('/')
def hello():
    nome_time = request.args['team_name']
    return get_team(nome_time)


app.run(host="0.0.0.0", port="7000", debug=True)

