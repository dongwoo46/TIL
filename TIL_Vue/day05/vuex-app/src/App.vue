<template>
  <div id="app">
    <!-- store안에 state안에 메시지 -->
    <!-- <h1>{{$store.state.message}}</h1> -->
    <h1>{{message}}의 길이는 {{messageLength}}</h1>
    <h2>X2 : {{doubleLength}}</h2>
    <!-- input누르고 엔터치면 changeMessage함수 실행 -->
    <input type="text" @keyup.enter='changeMessage' v-model="inputData">
  </div>
</template>

<script>


export default {
  name: 'App',
  data() {
    return {
      inputData : null
    }
  },
  methods: {
    changeMessage() {
      // newMessage가 inputdata로 바뀌고
      const newMessage = this.inputData
      // changeMessage라는 이름을 가진 action실행 
      this.$store.dispatch('changeMessage',newMessage)
      this.inputData = null
    }
  },
  components: {

  },
  computed: {
    message(){
      return this.$store.state.message
    },
    // getters에 있는거 사용할때  copmuted에서 사용해줌
    messageLength() {
      return this.$store.getters.messageLength
    },
    doubleLength() {
      return this.$store.getters.doubleLength
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
