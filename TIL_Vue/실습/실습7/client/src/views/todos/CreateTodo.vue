<template>
  <div>
    <input 
      type="text" 
      v-model.trim="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo: function () {
      let title = this.title
      // 2번 문제
      title = title.trim()
      if (!title) {
        alert('제목을 입력해라')
      }
      axios({
        method : 'post',
        url : `${API_URL}/todos/`,
        data: {title}
      })
      .then(()=> {
        this.$router.push({name: 'TodoList'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>
