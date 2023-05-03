<template>
  <div>
    <button @click="getDogImage">멍멍아 이리온</button><br><br>
    <img v-if="imgSrc" :src="imgSrc" alt="#"><br>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name:'DogComponent',
  data() {
    return {
      imgSrc: null,
    }
  },
  methods:{
    getDogImage() {
      const dogImageSearchURL = 'https://dog.ceo/api/breeds/image/random'
      
      axios({
        method: 'get',
        url: dogImageSearchURL
      })
        .then((response) => {
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  // create에서는 데이터나 요소 준비만 가능 
  created() {
    this.getDogImage()
    console.log('Dog created!')
    // const button = document.querySelector('button')
    // button.innerText = '멍멍!'
  },
  //키자마자 어떤 작업을 하고 싶은것 
  mounted() {
    console.log('Dog mounted!')
    const button = document.querySelector('button')
    button.innerText = '멍멍!'
  },
  updated() {
    console.log('새로운 멍멍이!')
    console.log('Dog updated!')
  }
}
</script>

<style>

</style>
