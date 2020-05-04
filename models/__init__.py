class Contato:
    def __init__(self, telefone, tipo_telefone, email, tipo_email):
        self.__telefone = telefone
        self.__tipo_telefone = tipo_telefone
        self.__email = email
        self.__tipo_email = tipo_email

    @property
    def get_telefone(self):
        return self.__telefone

    @property
    def get_tipo_telefone(self):
        return self.__tipo_telefone

    @property
    def get_email(self):
        return self.__email

    @property
    def get_tipo_email(self):
        return self.__tipo_email


class Identificacao:
    def __init__(self, nome_completo, cpf, sexo, estado_civil, data_nascimento, naturalidade):
        self.__nome_completo = nome_completo
        self.__cpf = cpf
        self.__sexo = sexo
        self.__estado_civil = estado_civil
        self.__data_nascimento = data_nascimento
        self.__naturalidade = naturalidade

    @property
    def get_nome_completo(self):
        return self.__nome_completo

    @property
    def get_cpf(self):
        return self.__cpf

    @property
    def get_sexo(self):
        return self.__sexo

    @property
    def get_estado_civil(self):
        return self.__estado_civil

    @property
    def get_data_nascimento(self):
        return self.__data_nascimento

    @property
    def get_naturalidade(self):
        return self.__naturalidade


class Pessoa:
    def __init__(self, identificacao, profissional, residencia, contato):
        self.__identificacao = identificacao
        self.__profissional = profissional
        self.__residencia = residencia
        self.__contato = contato

    @property
    def get_identificacao(self):
        return self.__identificacao

    @property
    def get_profissional(self):
        return self.__profissional

    @property
    def get_residencia(self):
        return self.__residencia

    @property
    def get_contato(self):
        return self.__contato


class Profissional:
    def __init__(self, profissao, formacao, renda):
        self.__profissao = profissao
        self.__formacao = formacao
        self.__renda = renda

    @property
    def get_profissao(self):
        return self.__profissao

    @property
    def get_formacao(self):
        return self.__formacao

    @property
    def get_renda(self):
        return self.__renda


class Residencia:
    def __init__(self, cep, tipo_endereco, logradouro, numero, bairro, complemento, municipio, estado):
        self.__cep = cep
        self.__tipo_endereco = tipo_endereco
        self.__logradouro = logradouro
        self.__numero = numero
        self.__bairro = bairro
        self.__complemento = complemento
        self.__municipio = municipio
        self.__estado = estado

    @property
    def get_cep(self):
        return self.__cep

    @property
    def get_tipo_endereco(self):
        return self.__tipo_endereco

    @property
    def get_logradouro(self):
        return self.__logradouro

    @property
    def get_numero(self):
        return self.__numero

    @property
    def get_bairro(self):
        return self.__bairro

    @property
    def get_complemento(self):
        return self.__complemento

    @property
    def get_municipio(self):
        return self.__municipio

    @property
    def get_estado(self):
        return self.__estado
