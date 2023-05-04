<template>
  <div>
    <!-- 입력하고 엔터키치면 createTodo함수 부르기 -->
    <input type="text" v-model.trim="todoTitle" @keyup.enter="createTodo">
  </div>
  

</template>

<script>
export default {
    name: 'TodoForm',
    data() {
        return {
            todoTitle: null,
        }
    },
    methods: {
        //액션 부르기 (actions 부르려면 dispatch)
        createTodo() {
            if (this.todoTitle) {
                this.$store.dispatch('createTodo', this.todoTitle)
            } else {
                alert('할일을 입력해 !')
            }
            this.todoTitle = null
        }
    }
}
</script>

<style>

</style>