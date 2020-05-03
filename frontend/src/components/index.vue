<template>
  <div>
    <b-col class="page-title-holder d-flex align-items-center">
      <h3 class="page-title">Cadastros</h3>
      <div class="page-title-controls">
        <b-button
          id="pessoa-new"
          @click="_new"
          variant="success"
          squared
          v-b-popover.hover.bottom="'Novo cadastro'">
          <font-awesome-icon icon="plus" />&nbsp;Novo
        </b-button>
      </div>
    </b-col>

    <b-col>&nbsp;</b-col>

    <b-table
      head-variant="light"
      light
      small
      striped
      hover
      :items="items" :fields="fields" v-bind:style="{cursor: 'pointer'}"
      @row-clicked="rowClicked">
      </b-table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'index',
  data () {
    return {
      fields: [
        {
          key: 'identificacao.nome_completo',
          label: 'Nome Completo'
        },
        {
          key: 'identificacao.cpf',
          label: 'CPF'
        },
        {
          key: 'identificacao.data_nascimento',
          label: 'Data de Nascimento'
        },
        {
          key: 'profissional.profissao',
          label: 'Profissão'
        }
      ],
      items: [],
      errors: []
    }
  },

  methods: {
    show (_id) {
      this.$router.push({ name: `${this.prefix}-show`, params: { _id } })
    },
    _new () {
      this.$router.push('pessoa/new')
      window.location.reload(true)
    },
    rowClicked (data) {
      console.log(data)
      this.$router.push(`pessoa/${data._id.$oid}/show`)
    }
  },

  created () {
    axios
      .get('http://localhost:5000/pessoas')
      .then(response => { this.items = response.data })
      .catch(e => { this.errors.push(e) })
  }
}
</script>

<style scoped>
>>> .limit-column {
  max-width: 200px;
  word-wrap: break-word;
}

b-table {
  text-align: center;
}
</style>
