class Profissional:
    def __init__(self, profissao, formacao, renda):
        self.__profissao = profissao
        self.__formacao = formacao
        self.__renda = renda

    @property
    def get_profissao(self):
        return self.__profissao

    @property
    def get_escolaridade(self):
        return self.__formacao

    @property
    def get_rendas(self):
        return self.__renda
