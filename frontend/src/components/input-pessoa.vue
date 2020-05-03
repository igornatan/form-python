<template>
  <div>
    {{model}}
    <b-col cols="12" sm="12" md="6" lg="6">
      <label>CPF</label>
      <b-form-input :mask="'###.###.###-##'" placeholder="000.000.000-00" class="form-control" :disabled="disabled" v-model="model.identificacao.cpf"/>
    </b-col>

    <b-col cols="12" sm="12" md="12" lg="6">
      <label>Nome Completo</label>
      <b-form-input placeholder="Digite seu nome" :disabled="disabled" v-model="model.identificacao.nome_completo"/>
    </b-col>

    <b-col cols="12" sm="12" md="12" lg="12" class="text-right">
      <b-button id="atividade-save" @click="save" size="sm" variant="success" v-if="!disabled">
        Salvar&nbsp;&nbsp;<font-awesome-icon icon="save"/>
      </b-button>
      <b-button id="atividade-edit" @click="edit" size="sm" variant="success" v-else-if="model._id">
        Editar&nbsp;&nbsp;<font-awesome-icon icon="edit"/>
      </b-button>
      <b-button id="atividade-back" @click="back" size="sm" variant="success">
        Voltar&nbsp;<font-awesome-icon icon="arrow-left"/>
      </b-button>
    </b-col>
  </div>
</template>

<script>
import Pessoa from '@/model/pessoa'
import axios from 'axios'

export default {
  name: 'pessoa',

  data () {
    return {
      // eslint-disable-next-line
      model: new Pessoa(),
      // model: 'testeeee',
      Pessoa: Pessoa,
      disabled: true
    }
  },

  methods: {
    show (_id) {
      axios.get(`http://localhost:5000/pessoas/${_id}`).then(response => {
        // eslint-disable-next-line
        this.model = new Pessoa(response.data)
      })
    },

    edit () {
      this.$router.push({name: 'pessoa-edit', params: { _id: this.model._id }}).catch(e => e)
      this.disabled = false
    },

    back () {
      this.$router.push('/index')
    },

    save () {
      console.log(this.model)
      // axios.put(`http://localhost:5000/pessoas/${this.model._id}`, 'testeeeeeeeeeee')
      axios({
        method: 'put',
        url: `http://localhost:5000/pessoas/${this.model._id.$oid}`,
        headers: {'content-type': 'application/json'},
        data: {
          identificacao: this.model.identificacao,
          contato: this.model.contato,
          residencia: this.model.residencia,
          profissional: this.model.profissional
        }
      })
    }
  },  

  mounted () {
    let _id = this.$route.params._id
    console.log(this.$route)
    console.log(this.$route.params)
    console.log(_id)

    if (_id) {
      this.show(_id)
    }
    this.disabled = this.$route.path.includes('/show')
    console.log(this.disabled)
  }
}
</script>

<style scoped>
  input, select {
    margin-bottom: 1em !important;
  }

  div.block_content {
    margin-left: 0;
  }

  >>> select.tools-types {
    display: none;
  }

  >>> button.pure-button.f-confirm {
    background-color: #118274;
    margin-left: 1em;
  }

  >>> button.pure-button {
    height: 2.4em;
    font-size: 1.4em;
  }

  >>> .pure-form input,
  >>> .pure-form select {
    height: 3em;
    font-size: 1.1em;
  }

  >>> .add-form,
  >>> .block.add-key {
    margin-top: 1em;
  }

  >>> .v-json-edit-icon-add {
    font-size: 3em;
  }

  >>> .block_content .val-input:focus {
    background: white;
  }
</style>
