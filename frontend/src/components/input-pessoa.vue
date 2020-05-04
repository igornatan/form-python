<template>
  <div>
    <b-tabs content-class="mt-3" fill>
      <b-tab title="Identificação" id="nav-identificacao">
        <b-col cols="12" sm="12" md="6" lg="6">
          <label for="identificacao-cpf">CPF</label>
          <b-form-input id="identificacao-cpf" :mask="'###.###.###-##'" placeholder="000.000.000-00" class="form-control" :disabled="disabled" v-model="model.identificacao.cpf"/>
        </b-col>

        <b-col cols="12" sm="12" md="6" lg="6">
          <label>Nome Completo</label>
          <b-form-input placeholder="Digite seu nome" :disabled="disabled" v-model="model.identificacao.nome_completo"/>
        </b-col>

         <b-col cols="12" sm="12" md="12" lg="6">
          <label>Sexo</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.identificacao.sexo"/>
        </b-col>

         <b-col cols="12" sm="12" md="12" lg="6">
          <label>Estado Civil</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.identificacao.estado_civil"/>
        </b-col>

         <b-col cols="12" sm="12" md="12" lg="6">
          <label>Data de Nascimento</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.identificacao.data_nascimento"/>
        </b-col>

         <b-col cols="12" sm="12" md="12" lg="6">
          <label>Naturalidade</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.identificacao.naturalidade"/>
        </b-col>
      </b-tab>

      <b-tab title="Residência">
         <b-col cols="12" sm="12" md="12" lg="6">
          <label>CEP</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.residencia.cep"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Tipo do Endereço</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.residencia.tipo_endereco"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Logradouro</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.residencia.logradouro"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Número</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.residencia.numero"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Bairro</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.residencia.bairro"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Complemento</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.residencia.complemento"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Município</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.residencia.municipio"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Estado</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.residencia.estado"/>
        </b-col>
      </b-tab>

      <b-tab title="Contato">
        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Telefone</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.contato.telefone"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Tipo Telefone</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.contato.tipo_telefone"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Email</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.contato.email"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Tipo Email</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.contato.tipo_email"/>
        </b-col>
      </b-tab>

      <b-tab title="Profissional">
        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Profissão</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.profissional.profissao"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Formação</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.profissional.formacao"/>
        </b-col>

        <b-col cols="12" sm="12" md="12" lg="6">
          <label>Renda</label>
          <b-form-input placeholder="" :disabled="disabled" v-model="model.profissional.renda"/>
        </b-col>
      </b-tab>

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
    </b-tabs>
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
      if (this.model._id) {
        axios({
          method: 'put',
          url: `http://localhost:5000/pessoas/${this.model._id.$oid}`,
          headers: {'Content-Type': 'application/json'},
          data: {
            identificacao: this.model.identificacao,
            contato: this.model.contato,
            residencia: this.model.residencia,
            profissional: this.model.profissional
          }
        }).then(response => {
          this.wait(2000)
          this.back()
        }).catch(e => e)
      } else {
        axios({
          method: 'post',
          url: 'http://localhost:5000/cadastrar',
          headers: {'Content-Type': 'application/json'},
          data: {
            identificacao: this.model.identificacao,
            contato: this.model.contato,
            residencia: this.model.residencia,
            profissional: this.model.profissional
          }
        }).then(response => {
          this.wait(2000)
          this.back()
        }).catch(e => e)
      }
    },

    wait (ms) {
      var start = new Date().getTime()
      var end = start
      while (end < start + ms) {
        end = new Date().getTime()
      }
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
  /*b-tabs {
    margin: 10px 700px;
  }*/

  label {
    display: inline-block;
    text-align: center;
    width: 200%;
  }

  input, select {
    /* width: 80%; */
    padding: 15px 22px;
    margin: 10px 450px;
    box-sizing: border-box;
    display: inline-block;
    margin-bottom: 1em;
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

  .nav-link {
    color: #494949 !important;
  }

  .nav-link:hover {
    color: #494949 !important;
  }

  li.tab:hover, a.disabled {
    cursor: not-allowed;
  }

  >>> input::placeholder {
    color: grey;
  }

  .btn-primary {
    background-color: transparent;
    border-color: black;
    color: black;
  }

  .btn-primary:hover {
    background-color: #D3D3D375;
    border-color: black;
    color: black;
  }

  .btn-primary:focus {
    background-color: transparent !important;
    border-color: grey !important;
    box-shadow: 0 0 0 0.2rem lightgrey !important;
    color: black !important;
  }

  .btn-primary:not(:disabled):not(.disabled):active {
    background-color: #D3D3D375;
    border-color: black;
    color: black;
  }
</style>
