import Vue from 'vue'
import VueRouter from 'vue-router'
import AllTodoPage from '../views/AllTodoPage.vue'
import TodayTodoPage from '../views/TodayTodoPage.vue'
import ImportantTodoPage from '../views/ImportantTodoPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'AllTodoPage',
    component: AllTodoPage,
  },
  {
    path: '/today',
    name: 'TodayTodoPage',
    component: TodayTodoPage,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
  },
  {
    path: '/important',
    name: 'ImportantTodoPage',
    component: ImportantTodoPage,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
