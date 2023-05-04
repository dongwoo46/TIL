<template>
  <div>
    <p>Todo... example</p>
    <p>{{todoitem.title}}</p>
  </div>
</template>

<script>
export default {
    name: 'TodoListItem',
    props: {
        //부모에게 받은 todoitem 등록
        todoitem: Object,
    }
}
</script>

<style>

</style>