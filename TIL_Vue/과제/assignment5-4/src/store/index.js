import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 0,
  },
  //getters는 state 첫번재 인자
  getters: {
    // state에 있는 것을 바꾸기때문에 state로 바꾸기

    counterDouble(state) {
      return state.counter * 2
    },
  },
  // mutations는 state의 첫번째 인자
  mutations: {
    // state에 있는 값을 바꾸는 거기 때문에 mutation
    INCREASE(state) {
      state.counter += 1
    },
    DECREASE(state) {
      state.counter -= 1
    },
  },
  actions: {
    
  },
  modules: {
  },
})
