import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store'
  },
  //computed와 비슷
  getters: {
    messageLength(state) {
      return state.message.length
    },
    doubleLength(state,getters) {
      return getters.messageLength * 2
    }
  },
  mutations: {
    // mutations에서는 state가 앞에 들어감
    CHANGE_MESSAGE(state,payload) {
      // console.log(state)
      // console.log(message)
      state.message = payload
    }
  },
  actions: {
    //여기서 message는 app.vue에서 받은 newMessage
    changeMessage(context, message){
      // context를 commit해서 CHANGE_MESSAGE라는 mutation사용
      context.commit('CHANGE_MESSAGE',message)
    }
  },
  modules: {
  }
})
