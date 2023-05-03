<template>
  <div>
    <h3>This is child component</h3>
    <p>{{staticProps}}</p>
    <p>{{myProps}}</p>
    <!-- 클리할 때마다 childToParent메서드 실행 -->
    <button @click="childToParent">클릭!</button> 
    <!-- 엔터 칠때마다 childInput실행 -->
    <input type="text" v-model="childInputData" @keyup.enter="childInput">
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  data: function() {
    return {
      childInputData :null,
    }
  },
  props : {
    staticProps: String,
    myProps: String,
  },
  methods: {
    childToParent : function() {
      this.$emit('child-to-parent','child Data') // child-to-parent이벤트 발생
    },
    // $emit 을 통해 부모 컴포넌트에 child-input발생 
    childInput: function() {
      this.$emit('child-input', this.childInputData)
      this.childInputData = ""
    }
  }
}
</script>

<style>
  
</style>
