<template>
  <div class="home">
    <h1>점심메뉴</h1>
    <!-- <HelloWorld msg="점심메뉴"/> -->
    <button @click="pickLunch">pick Lunch</button>
    <p>{{lunch}}</p>
    
    <br>
    <h2> 로또를 뽑아 보자</h2>
    <button @click='pickLotto'>pick Lotto</button>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import _ from 'lodash'
export default {
  name: 'LunchView',
  data() {
    return {
      menu : ["국밥", "참치", "사람", "인간", "뇌", ],
      lunch : null
    }
  },
  components: {
    // HelloWorld
  },
  methods: {
    pickLunch() {
      this.lunch = _.sample(this.menu)
    },
    pickLotto() {
      this.$router.push({name:'lotto'})
    }
  }
}
</script>
