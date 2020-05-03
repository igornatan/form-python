class Base {
  constructor (model = {}) {
    for (let key in model) {
      this[key] = model[key]
    }
  }
}

export default Base
