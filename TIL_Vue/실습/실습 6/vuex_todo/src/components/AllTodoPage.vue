<template>
  <div>
    <h1>모든 할 일</h1>
    <hr>
    <TodoList :todos="allTodoList"/>
  </div>
</template>

<script>
import TodoCreateForm from '@/components/TodoCreateForm.vue'
import TodoList from '@/components/TodoList.vue'
export default {
  components : {
    TodoList,
    TodoCreateForm,
  },
  computed: {
    allTodoList() {
      return this.$store.state.todo.todos
    }
  }
}
</script>

<style>

</style>