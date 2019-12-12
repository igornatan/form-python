class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_data_nascimento(self):
        return self.data_nascimento

