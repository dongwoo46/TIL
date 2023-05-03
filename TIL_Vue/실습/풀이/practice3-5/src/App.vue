<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>parentData : {{parentData}}</p>
    <p>childData: {{childData}}</p>
    <!-- parent에서 입력값이 변경했을때 발생하는 이벤트  child에서 입력값이 변경했을 때 발생하는 이벤트-->
    <!-- parent로 값을 props하고 parent에서 입력값을 받아오기 -->
    <AppParent :app-data="appData" @parent-input-change="onParentInputChange" @child-input-change="onChildInputChange"/>

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
      appData: null,
      parentData: null,
      childData: null,
    }
  },
  methods: {
    // parent에 입력값의 변화가 생기면 현재 parentData값을 parent의 입력값으로 바꾸기
    onParentInputChange: function(parentInputData) {
      this.parentData = parentInputData
    },
    // child에 입력값의 변화가 있으면 childData의 값을 현재 child의 입력값으로 바꾸기
    onChildInputChange: function(childInputData) {
      this.childData = childInputData
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
