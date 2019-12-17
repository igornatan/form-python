from flask import Flask, jsonify, request, render_template, url_for, redirect, send_from_directory
from flask_pymongo import PyMongo

# Importando as classes
from Pessoa import Pessoa
from Identificacao import Identificacao
from Residencia import Residencia
from Contato import Contato
from Profissional import Profissional

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'form_rest_h'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/form_rest_h'

mongo = PyMongo(app)


@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
    form_rest_h = mongo.db.form_rest_h
    output = []

    for q in form_rest_h.find():
        output.append({'identificacao': q['identificacao'],
                        'residencia': q['residencia'],
                        'contato': q['contato'],
                        'profissional': q['profissional']})
    return render_template('listar.html', output=output, titulo='Pessoas')


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Cadastro')


@app.route('/cadastrar', methods=['POST'])
def cadastrar_pessoa():
    nome_completo = request.form['nome_completo']
    cpf = request.form['cpf']
    sexo = request.form['sexo']
    estado_civil = request.form['estado_civil']
    data_nascimento = request.form['data_nascimento']
    naturalidade = request.form['naturalidade']
    identificacao = Identificacao(nome_completo, cpf, sexo, estado_civil, data_nascimento, naturalidade)

    cep = request.form['cep']
    tipo_endereco = request.form['tipo_endereco']
    logradouro = request.form['logradouro']
    numero = request.form['numero']
    bairro = request.form['bairro']
    complemento = request.form['complemento']
    municipio = request.form['municipio']
    residencia = Residencia(cep, tipo_endereco, logradouro, numero, bairro, complemento, municipio)

    telefone = request.form['telefone']
    tipo_telefone = request.form['tipo_telefone']
    email = request.form['email']
    tipo_email = request.form['tipo_email']
    contato = Contato(telefone, tipo_telefone, email, tipo_email)

    profissao = request.form['profissao']
    formacao = request.form['formacao']
    renda = request.form['renda']
    profissional = Profissional(profissao, formacao, renda)

    form_rest_h = mongo.db.form_rest_h
    form_rest_h.insert({'identificacao': {'nome_completo': identificacao.get_nome_completo, 
                                        'cpf': identificacao.get_cpf,
                                        'sexo': identificacao.get_estado_civil,
                                        'estado_civil': identificacao.get_estado_civil,
                                        'data_nascimento': identificacao.get_data_nascimento,
                                        'naturalidade': identificacao.get_naturalidade},
                        'residencia': {'cep': residencia.get_cep,
                                        'tipo_endereco': residencia.get_tipo_endereco,
                                        'logradouro': residencia.get_logradouro,
                                        'numero': residencia.get_numero,
                                        'bairro': residencia.get_bairro,
                                        'complemento': residencia.get_complemento,
                                        'municipio': residencia.get_municipio},
                        'contato': {'telefone': contato.get_telefone,
                                        'tipo_telefone': contato.get_telefone,
                                        'email': contato.get_email,
                                        'tipo_email': contato.get_tipo_email},
                        'profissional': {'profissao': profissional.get_profissao,
                                        'formacao': profissional.get_formacao,
                                        'renda': profissional.get_renda}
                                        })

    return redirect(url_for('listar_pessoas'))


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

# @app.route('/uploads/<nome_arquivo>')
# def imagem(nome_arquivo):
#     return send_from_directory('uploads', nome_arquivo)


if __name__ == '__main__':
    app.run(debug=True)
