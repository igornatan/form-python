import Base from '@/model/base'

class Pessoa extends Base {
  constructor (model) {
    super(model || blank)
  }
}

export default Pessoa

const blank = {
  identificacao: null,
  profissional: null,
  residencia: null,
  contato: null
}

export {}
