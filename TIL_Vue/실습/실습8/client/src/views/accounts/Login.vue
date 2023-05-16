<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="userdata.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" @keyup.enter="login" v-model = "userdata.password">
    </div>
    <button @click='login'>로그인</button>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'LoGin',
  data: function () {
    return {
      username : null,
      password : null,
    }
  },
  methods: {
    login: function (res) {
      console.log(res)
    }
  }
}
</script>
