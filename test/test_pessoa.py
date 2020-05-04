import json

from loguru import logger

# Importando as classes
from models import Pessoa
from models import Identificacao
from models import Residencia
from models import Contato
from models import Profissional


def main():
    casa = Residencia('88888-000', 'Avenida', 'Getúlio Vargas', '80', 'Centro', None, 'Chapecó', 'SC')
    contato = Contato('(49) 99999-9999', 'Particular', 'teste@teste.com', 'Comercial')
    identificacao = Identificacao('Igor Bagio', '111.222.333-44', 'Masculino', 'Solteiro', '19/08/1999', 'Xaxim/SC')
    profissional = Profissional('Desenvolvedor', 'Graduando', '1.000,00')
    Igor = Pessoa(identificacao, profissional, casa, contato)

    logger.debug(json.dumps(Igor.__dict__, indent=4))


if __name__ == '__main__':
    main()