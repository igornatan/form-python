class Residencia:
    def __init__(self, cep, tipo_endereco, logradouro, numero, bairro, complemento, municipio):
        self.__cep = cep
        self.__tipo_endereco = tipo_endereco
        self.__logradouro = logradouro
        self.__numero = numero
        self.__bairro = bairro
        self.__complemento = complemento
        self.__municipio = municipio

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
