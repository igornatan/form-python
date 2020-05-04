# Orientação a Objetos

## Cadastro de Pessoas

<p>Implementação de uma aplicação que faça cadastro de pessoas.</p>

### Tecnologias utilizadas

> Python

> Vue.js

> Flask

> MongoDB

## Dependências

> Node.js

> Python 3.6

> Pipenv

> MongoDB

## Build

### Python

```bash
	$ pipenv install
	$ pipenv shell
	$ python3 app.py
```

### Frontend

```bash
	$ cd frontend/
	$ npm install
	$ npm run dev
```

## Endpoints

**POST** /cadastrar

Persiste as informações no banco de dados.

Body:

```json
{
    "identificacao": {
        "nome_completo": "Joãozinho da Silva",
        "cpf": "738.275.891-50",
        "sexo": "Masculino",
        "estado_civil": "Casado",
        "data_nascimento": "13/11/1987",
        "naturalidade": "Goiânia/GO"
    },
    "contato": {
        "telefone": "(62) 3548-4701",
        "tipo_telefone": "Particular",
        "email": "teste@gmail.com",
        "tipo_email": "Particular"
    },
    "residencia": {
        "cep": "74483-230",
        "tipo_endereco": "Casa",
        "logradouro": "Rua Dona Inês",
        "numero": "926",
        "bairro": "Parque Industrial João Braz",
        "complemento": "Nd",
        "municipio": "Goiânia",
        "estado": "GO"
    },
    "profissional": {
        "profissao": "Carpinteiro",
        "formacao": "Ensino Médio",
        "renda": "R$ 1000,00"
    }
}
```

**GET** /pessoas

Retorna um array com todos os cadastros do banco de dados.

**GET** /pessoas/<id_pessoa>

Retorna um cadastro específico.

**PUT** /pessoas/<id_pessoa>

Atualiza um cadastro específico com novas informações.