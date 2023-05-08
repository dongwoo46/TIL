<template>
  <li>
    <i v-if="isCompleted" class="bi bi-check-circle clickable"></i>
    <i v-else class="bi bi-circle clickable"></i>
    <span class="clickable">{{content}}</span>
    <button class="btn ms-auto">
        <i v-if="isImportant" class="bi bi-star-fill"> </i>
        <i v-else class="bi bi-star"> </i>
    </button>
  </li>
</template>

<script>
export default {
    props: {
        todo : {
            type:Object,
            required: true,
        }
    },
    computed : {
        content() {
            return this.todo.content
        },
        isCompleted() {
            return this.todo.iscompleted
        },
        isImportant() {
            return this.todo.isImportant
        },
    },
}
</script>

<style>
.clickable{
    cursor: pointer;
}
</style>