from flask import Flask, jsonify, request, render_template, url_for, redirect, send_from_directory
from flask_pymongo import PyMongo
from flask_cors import CORS
from loguru import logger
from bson import ObjectId
from bson.json_util import dumps
import json

# Importando as classes
from models.Pessoa import Pessoa
from models.Identificacao import Identificacao
from models.Residencia import Residencia
from models.Contato import Contato
from models.Profissional import Profissional

app = Flask(__name__)
CORS(app)

app.config['MONGO_DBNAME'] = 'register'
app.config['MONGO_URI'] = 'mongodb://192.168.10.132:27017/register'

mongo = PyMongo(app)


@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
    register = mongo.db.register
    output = []

    for q in register.find():
        output.append({
            '_id': q['_id'],
            'identificacao': q['identificacao'],
            'residencia': q['residencia'],
            'contato': q['contato'],
            'profissional': q['profissional']
        })
    return dumps(output)


@app.route('/pessoas/<id_pessoa>', methods=['GET'])
def get_pessoa(id_pessoa):
    register = mongo.db.register
    pessoa = register.find_one({'_id': ObjectId(id_pessoa)})
    return dumps(pessoa)


@app.route('/pessoas/<id_pessoa>', methods=['PUT'])
def edit_pessoa(id_pessoa):
    data = json.loads(request.data.decode('utf-8'))
    logger.debug(json.dumps(data, indent=4))
    register = mongo.db.register
    register.update({'_id': ObjectId(id_pessoa)}, {'$set': json.loads(request.data)})
    # logger.debug("Pessoa", pessoa)
    return request.data.decode('utf-8')


@app.route('/cadastrar', methods=['POST'])
def cadastrar_pessoa():
    """ Realiza o cadastro de uma pessoa com as
    informações vindas do formulário.
    :return:
    """

    logger.debug(request.data.decode('utf-8'))

    pessoa = json.loads(request.data.decode('utf-8'))

    identificacao = Identificacao(
        nome_completo=pessoa['identificacao']['nome_completo'],
        cpf=pessoa['identificacao']['cpf'],
        sexo=pessoa['identificacao']['sexo'],
        estado_civil=pessoa['identificacao']['estado_civil'],
        data_nascimento=pessoa['identificacao']['data_nascimento'],
        naturalidade=pessoa['identificacao']['naturalidade']
    )

    residencia = Residencia(
        cep=pessoa['residencia']['cep'],
        tipo_endereco=pessoa['residencia']['tipo_endereco'],
        logradouro=pessoa['residencia']['logradouro'],
        numero=pessoa['residencia']['numero'],
        bairro=pessoa['residencia']['bairro'],
        complemento=pessoa['residencia']['complemento'],
        municipio=pessoa['residencia']['municipio'],
        estado=pessoa['residencia']['estado']
    )

    contato = Contato(
        telefone=pessoa['contato']['telefone'],
        tipo_telefone=pessoa['contato']['tipo_telefone'],
        email=pessoa['contato']['email'],
        tipo_email=pessoa['contato']['tipo_email']
    )

    profissional = Profissional(
        profissao=pessoa['profissional']['profissao'],
        formacao=pessoa['profissional']['formacao'],
        renda=pessoa['profissional']['renda']
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
    return dumps(cadastro)


if __name__ == '__main__':
    app.run(debug=True)
