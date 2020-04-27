<template>
  <div>

  <b-col cols="12" sm="12" md="6" lg="6">
    <label>CPF</label>
    <b-form-input :mask="'###.###.###-##'" placeholder="000.000.000-00" class="form-control" :disabled="disabled" v-model="text2" />
  </b-col>

  <b-col cols="12" sm="12" md="12" lg="6">
    <label>Nome Completo</label>
    <b-form-input placeholder="Digite seu nome" :disabled="disabled" v-model="text1" />
  </b-col>

    </div>

<!--  <div class="input-text">-->
<!--    <div class="card-title">Nome Completo</div>-->
<!--    <b-form-input v-model="text1" placeholder="Digite seu nome"></b-form-input>-->

<!--    <div class="card-title">Nome Completo</div>-->
<!--    <b-form-input v-model="text2" placeholder="Digite seu nome"></b-form-input>-->

<!--    <div class="card-title">Nome Completo</div>-->
<!--    <b-form-input v-model="text3" placeholder="Digite seu nome"></b-form-input>-->

<!--    <div class="card-title">Nome Completo</div>-->
<!--    <b-form-input v-model="text4" placeholder="Digite seu nome"></b-form-input>-->
<!--  </div>-->
</template>

<script>
    export default {
        name: "novo",
        data() {
          return {
            text1: '',
            text2: '',
            text3: '',
            text4: '',
          }
        }

    }
</script>

<style scoped>
.input-text{
  width: 35%;
  margin-top: 100px;
  margin-bottom: 100px;
  margin-right: 150px;
  margin-left: 50px;
}
  .card-title{
    text-align: left;
  }
</style>
