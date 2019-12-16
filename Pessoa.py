class Pessoa:
    def __init__(self, identificacao, profissional, relacionamento, residencia, contato):
        self.__identificacao = identificacao
        self.__profissional = profissional
        self.__relacionamento = relacionamento
        self.__residencia = residencia
        self.__contato = contato

    @property
    def get_identificacao(self):
        return self.__identificacao

    @property
    def get_profissional(self):
        return self.__profissional

    @property
    def get_relacionamento(self):
        return self.__relacionamento

    @property
    def get_residencia(self):
        return self.__residencia

    @property
    def get_contato(self):
        return self.__contato
