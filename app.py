from flask import Flask, jsonify, request, render_template, url_for, redirect, send_from_directory
from flask_pymongo import PyMongo
from flask_cors import CORS
from loguru import logger

# Importando as classes
from models.Pessoa import Pessoa
from models.Identificacao import Identificacao
from models.Residencia import Residencia
from models.Contato import Contato
from models.Profissional import Profissional

app = Flask(__name__)
CORS(app)

app.config['MONGO_DBNAME'] = 'register'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/register'

mongo = PyMongo(app)


@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
    register = mongo.db.register
    output = []

    for q in register.find():
        output.append({
            'identificacao': q['identificacao'],
            'residencia': q['residencia'],
            'contato': q['contato'],
            'profissional': q['profissional']
        })
    # return render_template('listar.html', output=output, titulo='Cadastros')
    return jsonify(output)


@app.route('/cadastrar', methods=['POST'])
def cadastrar_pessoa():
    """ Realiza o cadastro de uma pessoa com as
    informações vindas do formulário.
    :return:
    """
    identificacao = Identificacao(
        nome_completo=request.form['nome_completo'],
        cpf=request.form['cpf'],
        sexo=request.form['sexo'],
        estado_civil=request.form['estado_civil'],
        data_nascimento=request.form['data_nascimento'],
        naturalidade=request.form['naturalidade']
    )

    residencia = Residencia(
        cep=request.form['cep'],
        tipo_endereco=request.form['tipo_endereco'],
        logradouro=request.form['logradouro'],
        numero=request.form['numero'],
        bairro=request.form['bairro'],
        complemento=request.form['complemento'],
        municipio=request.form['municipio'],
        estado=request.form['estado']
    )

    contato = Contato(
        telefone=request.form['telefone'],
        tipo_telefone=request.form['tipo_telefone'],
        email=request.form['email'],
        tipo_email=request.form['tipo_email']
    )

    profissional = Profissional(
        profissao=request.form['profissao'],
        formacao=request.form['formacao'],
        renda=request.form['renda']
    )

    cadastro = {
        'identificacao': {
            'nome_completo': identificacao.get_nome_completo,
            'cpf': identificacao.get_cpf,
            'sexo': identificacao.get_estado_civil,
            'estado_civil': identificacao.get_estado_civil,
            'data_nascimento': identificacao.get_data_nascimento,
            'naturalidade': identificacao.get_naturalidade
        },
        'residencia': {
            'cep': residencia.get_cep,
            'tipo_endereco': residencia.get_tipo_endereco,
            'logradouro': residencia.get_logradouro,
            'numero': residencia.get_numero,
            'bairro': residencia.get_bairro,
            'complemento': residencia.get_complemento,
            'municipio': residencia.get_municipio,
            'estado': residencia.get_estado
        },
        'contato': {
            'telefone': contato.get_telefone,
            'tipo_telefone': contato.get_telefone,
            'email': contato.get_email,
            'tipo_email': contato.get_tipo_email
        },
        'profissional': {
            'profissao': profissional.get_profissao,
            'formacao': profissional.get_formacao,
            'renda': profissional.get_renda
        }
    }

    register = mongo.db.register
    register.insert(cadastro)
    return jsonify(cadastro)


@app.route('/vue')
def test_vue():
    return render_template('novo.vue')


if __name__ == '__main__':
    app.run(debug=True)
