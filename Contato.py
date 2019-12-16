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
