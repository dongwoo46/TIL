<template>
  <div id="app">
    <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase()">increase +</button>
    <button @click="decrease()">decrease -</button>
    </div>
  </div>
</template>

<script>


export default {
  name: 'App',
  methods:{
    //mutations 바꾸는 건 commit을 통해 mutations에 있는 함수 호출
    increase() {
      this.$store.commit('INCREASE')
    },
    decrease() {
      this.$store.commit('DECREASE')
    }
  },
  // getters와 state의 값을 가지고 옮
  computed:{
    counterDouble() {
      return this.$store.getters.counterDouble
    },
    counter() {
      return this.$store.state.counter
    }

  },
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
