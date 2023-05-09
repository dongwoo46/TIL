import Vue from 'vue'
import VueRouter from 'vue-router'
import FirstView from '../views/FirstView.vue'
import SecondView from '..views/SecondView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'first',
    component: 'FirstView',
  },
  {
    path: '/second',
    name: 'SecondView',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/SecondView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
