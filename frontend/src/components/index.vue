<template>
  <div>
    <b-table striped hover :items="items" :fields="fields"></b-table>
  </div>
</template>

<script>
  import axios from 'axios';

    export default {
        name: "index",
        data() {
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

        created() {
          axios
            .get('http://localhost:5000/pessoas')
            .then(response => {this.items = response.data})
            .catch(e => {this.errors.push(e)})
        }

    }
</script>

<style scoped>

</style>
