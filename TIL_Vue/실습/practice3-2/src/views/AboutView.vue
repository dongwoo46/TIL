<template>
  <div class="about">
    <h1>로또</h1>
    <button @click="getLotto">Get Lucky Numbers</button>
    <p>{{selectedNumbers}}</p>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'LottoView',
  data() {
    return {
      selectedNumbers : null
    }
  },
  methods: {
    getLotto() {
      this.selectedNumbers = _.sampleSize(_.range(0,46),6)
    }
  }
}
</script>

<style>

</style>
