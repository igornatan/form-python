import Base from '@/model/base'

class Pessoa extends Base {
  constructor (model) {
    super(model || blank)
  }
}

export default Pessoa

const blank = {
  identificacao: {
	nome_completo: null,
	cpf: null,
	sexo: null,
	estado_civil: null,
	data_nascimento: null,
	naturalidade: null
  },
  profissional: {
	profissao: null,
	formacao: null,
	renda: null
  },
  residencia: {
	cep: null,
	tipo_endereco: null,
	logradouro: null,
	numero: null,
	bairro: null,
	complemento: null,
	municipio: null,
	estado: null
  },
  contato: {
	telefone: null,
	tipo_telefone: null,
	email: null,
	tipo_email: null
  }
}

export {}
