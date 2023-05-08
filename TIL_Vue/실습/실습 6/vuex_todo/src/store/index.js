import Vue from 'vue'
import Vuex from 'vuex'
// 모듈 사용을 위한 import
import todo from './modules/todo.js'
// import 'bootstrap/dist/css/bootstrap.min.css'
// import 'bootstrap-icons/font/bootstrap-icons.css'
Vue.use(Vuex)

export default new Vuex.Store({
  // Module 사용하기
  modules: {
    todo,
  }
})
