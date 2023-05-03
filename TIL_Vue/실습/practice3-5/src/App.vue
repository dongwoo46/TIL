<template>
  <div id="app">
    <h1>App</h1>
    <input  id="msg" type="number" v-model.number='msg'>
    <p>{{msg}}</p>
    <AppParent :appMsg="msg"/>
    
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {

    AppParent,
  },
  data: function() {
    return {
      msg : ''
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
