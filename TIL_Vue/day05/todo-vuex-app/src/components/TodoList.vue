<template>
  <div>
    <!-- 부모가 자식에게 데이터(todo데이터) 내려주기 -->
    <!-- todoitem이라는 이름으로 자식에게 데이터 todo보내주기 -->
    <TodoListItem v-for="(todo,index) in todos" :key="index" :todoitem="todo"/>

  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'
export default {
    name: 'TodoList',
    components: {
        TodoListItem,
    },
    //state에 있는건 computed이용
    computed: {
        todos() {
            return this.$store.state.todos
        },
    }
}
</script>

<style>

</style>