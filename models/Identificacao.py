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
