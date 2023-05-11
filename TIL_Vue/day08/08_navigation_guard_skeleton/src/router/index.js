import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView'
import NotFound404 from '@/views/NotFound404'
import DogView from '@/views/DogView'

Vue.use(VueRouter)

const isLoggedIn = true

const routes = [
  {
    path: '/404',
    name: 'NotFound404',
    component : NotFound404,
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path : '/login',
    name: 'login',
    component: LoginView,
    // 라우터 가드
    beforeEnter(to, from, next) {
      if (isLoggedIn ===true) {
        console.log('이미 로그인 함')
        next({name:'home'})
      } else {
        next() //로그인  안되어 있으면 로그인 페이지로 이동
      }
    }
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component : DogView,
  },
  {
    path: '*', // 위에 해당하지 않는 모든 것은 404로 보내라!
    redirect: '/404',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


// 전역 가드 
// router/index.js
// router.beforeEach((to, from, next) => {
//   // CODE HERE
//   //로그인 여부
//   // const isLoggedIn = true //로그인 됨
//   const isLoggedIn = false // 로그인 안됨
//   //로그인 필요한 페이지 지정
//   // const authPages = ['hello','about','home']
//   const allowAuthPages = ['login']
//   //앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
//   // const isAuthRequired = authPages.includes(to.name)
//   const isAuthRequired = !allowAuthPages.includes(to.name)
  
//   if (isAuthRequired && !isLoggedIn) {
//     console.log('login으로 이동')
//     next({name:'login'})
//   } else {
//     console.log('to로 이동!') //로그인이 되어 있거나 로그인이 필요없으면
//     next()
//   }
// })
export default router
