""" pip install virtualenv
/* criar pasta do projeto "mkdir nome_da_pasta"
/* acessar a pasta e iniciar o virtualenv "virtualenv .venv"
/* source .venv/bin/activate
/* após acessar o ambiente env instalar o flask
/* pip install flask
/* criar arquivo requeriments "touch requirements.txt"
/* colocar a versão usada do flask no requeriments"""

from flask import Flask, jsonify, request

app = Flask(__name__)

troco = [
    {
        'notas':'100', '50', '10', '5', '1'
    },
    {
        'moedas': '0.50', '0.10', '0.05', '0.01'
    }
]

@app.route('/', methods=['GET'])
def home():
    return jsonify(troco), 200

@app.route('/<int:notas>', methods=['GET'])
def notas_in(notas):
    notas_in =[nota for nota in troco if nota['notas']==notas]
    return jsonify(moedas_in), 200

@app.route('/<int:moedas>', methods=['GET'])
def moedas_in(moedas):
    moedas_in =[moeda for moeda in troco if troc['moedas']==moedas]
    return jsonify(moedas_in), 200


@app.route('/<int:troco>', methods =['GET'])
def troco_in(troco):
    for nota in troco:
        if nota['notas']== troco['notas']:
            return jsonify(nota), 200
    return jsonify({'ERROR'}), 404
    for moeda in troco:
        if moeda['moedas']==troco['moedas']:
            return jsonify(moeda), 200
    return jsonify({'ERROR'}), 404

@app.route('/', methods =['POST'])
def paga():
    for paga in troco:
        if paga['notas']== paga - troco['notas']
    for paga in troco:
        if paga['moedas'] == paga - troco['moedas']
    paga = request.get_json()
    paga.append(paga)

    return jsonify(paga), 201

@app.route('/', methods =['PUT'])
def recebe(troco):
    for trocos in troco:
        if trocos['notas'] == troco:
            trocos['notas'] = request.json().get('notas')
    for trocos in troco:
        if trocos['moedas'] == troco:
            trocos['moedas'] = request.json().get('moedas')

    return jsonify({'ERROR'}), 404

@app.route('/', methods = ['DELETE'])
def remover(troco):
    index = troco -1
    del troco[index]

    return jsonify({'REMOVIDO COM SUCESSO'})

if __name__=='__main__':
    app.run(debug=True)