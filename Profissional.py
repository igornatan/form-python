class Profissional:
    def __init__(self, profissao, escolaridade, renda):
        self.__profissao = profissao
        self.__escolaridade = escolaridade
        self.__renda = renda

    @property
    def get_profissao(self):
        return self.__profissao

    @property
    def get_escolaridade(self):
        return self.__escolaridade

    @property
    def get_rendas(self):
        return self.__renda
