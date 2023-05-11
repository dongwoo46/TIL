import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HappeedView from '../views/HappeedView.vue'
import HapplingView from '../views/HapplingView.vue'
import NotFound from '../views/404View.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/happeed',
    name: 'Happeed',
    component: HappeedView
  },
  {
    path: '/happling',
    name: 'Happling',
    component: HapplingView
  },
  {
    path: '/notfound',
    name: 'NotFound',
    component: NotFound
  },
  {
    path: '*',
    redirect: '/notfound'
  }
]



const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to,from, next)=> {
  if (from.name === 'Happling' && to.name === 'Happeed'){
    alert('퇴화 안됨')
    return
  }

  !to.name? next({name:'NotFound'}):next()
  console.log(from.name, '온곳')
  console.log(to.name, '가려는곳')
  next()
})



export default router
