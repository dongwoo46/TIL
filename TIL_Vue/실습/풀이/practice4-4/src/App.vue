<template>
  <div id="app">
    <h1>SSAFY TUBE</h1>
    <section v-if="isfirst">
      <iframe :src="first" width="800" height="600" frameborder="0"></iframe>
    </section>
    <p>{{introduction}}</p>
  </div>
</template>

<script>

import axios from 'axios'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const URL='https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  data() {
    return {
      first : null,
      introduction : null,
    }
  },
  created() {
    axios.get(URL, {
      params: {
        key: API_KEY,
        type: 'video',
        part: 'snippet',
        q: '코딩노래',
      }
    })
    .then(res => {
      console.log(res)
      this.first = `https://www.youtube.com/embed/${res.data.items[0].id.videoId}`
      this.introduction = res.data.items[0].snippet.title
    })
    .catch(error => console.log(error))
  },
  computed: {
    isfirst() {
      // return this.first.length
      return this.first != null
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
