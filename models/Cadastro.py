# from Pessoa import Pessoa
# from Residencia import Residencia
# from Contato import Contato
# from Identificacao import Identificacao
# from Profissional import Profissional

# from flask import Flask, jsonify, request, render_template, url_for, redirect, send_from_directory
# from flask_pymongo import PyMongo

# from Pessoa import Pessoa

# app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'form_rest'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/form_rest'

# mongo = PyMongo(app)


# class Cadastrar(object):

#     @app.route('/novo')
#     def novo(self):
#         return render_template('novo.html', titulo='Novo Cadastro')
    
#     @app.route('/identificacao')
#     def cadastrar_identificacao(self):
#         # nome_completo = 'Igor Natan M. Bagio'
#         # cpf = '111.222.333-44'
#         # sexo = 'Masculino'
#         # estado_civil = 'Solteiro'
#         # data_nascimento = '19/08/1999'
#         # naturalidade = 'Xaxim/SC'
#         nome_completo = request.form['nome_completo']
#         cpf = request.form['cpf']
#         sexo = request.form['sexo']
#         estado_civil = request.form['estado_civil']
#         data_nascimento = request.form['data_nascimento']
#         naturalidade = request.form['naturalidade']
        
#         identificacao = Identificacao(nome_completo, cpf, sexo, estado_civil, data_nascimento, naturalidade)

#         return identificacao

#     def cadastrar_residencia(self):
#         cep = '88888-000'
#         tipo_endereco = 'Residencial'
#         logradouro = 'Fernando Machado'
#         numero = '80'
#         bairro = ''
