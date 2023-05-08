<template>
    <form @submit="createTodo">
      <input type="text" v-model='content' placeholder="할일을 작성해라">
    </form>
</template>

<script>
export default {
    data() {
        return {
            content: '',
        }
    },
    methods:{
        createTodo(event) {
            event.preventDefault() // 새로고침 막기!!
            const data = {
                content : this.content,
            }
            this.$store.dispatch("todo/createTodo", data)
            this.content = ''
        }
    }
}
</script>

<style>

</style>