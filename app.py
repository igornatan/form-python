from flask import Flask, jsonify, request, render_template, url_for, redirect, send_from_directory
from flask_pymongo import PyMongo

from Pessoa import Pessoa

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'form_rest'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/form_rest'

mongo = PyMongo(app)


@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
    form_db = mongo.db.form_rest
    output = []

    for q in form_db.find():
        output.append({'name': q['name'],
                       'cpf': q['cpf'],
                       'data_nascimento': q['data_nascimento']})
    return render_template('listar.html', output=output, titulo='Pessoas')


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Cadastro')


@app.route('/cadastrar', methods=['POST'])
def cadastrar_pessoa():
    nome = request.form['nome']
    cpf = request.form['cpf']
    data_nascimento = request.form['data_nascimento']
    pessoa = Pessoa(nome, cpf, data_nascimento)

    form_db = mongo.db.form_rest
    form_db.insert({'name': pessoa.get_nome(),
                    'cpf': pessoa.get_cpf(),
                    'data_nascimento': pessoa.get_data_nascimento()})

    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', titulo='Bem vindo ao Form')


# @app.route('/table')
# def table():
#     form_db = mongo.db.form_rest
#     output = []

#     for q in form_db.find():
#         output.append({'name': q['name'], 
#                        'cpf': q['cpf'], 
#                        'data_nascimento': q['data_nascimento']})
#     return render_template('table.html', output=output)

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)


if __name__ == '__main__':
    app.run(debug=True)
