import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import pessoa from '@/components/input-pessoa'
import index from '@/components/index'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', name: 'HelloWorld', component: HelloWorld },
    { path: '/index', name: 'index', component: index },
    { path: '/pessoa/new', name: 'pessoa-new', component: pessoa },
    { path: '/pessoa/:_id/show', name: 'pessoa-show', component: pessoa },
    { path: '/pessoa/:_id/edit', name: 'pessoa-edit', component: pessoa }
    // { path: '/pessoa/5eac6769dfdbc5bb396af71e/edit', name: 'pessoa-test', component: pessoa }
  ]
})
