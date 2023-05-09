<template>
    <div>
        <h1>로또</h1>
        <button @click="getNums">Get Lucky Numbers</button>
        <p>{{selectedNums}}</p>
    </div>
</template>

<script>
import _ from 'lodash'
export default {
    name: 'TheLotto',
    data() {
        return {
            selectedNums: []
        }
    },
    methods: {
        getNums() {
            const numbers = _.range(1,46)
            // 만약 특정한 곳에서 값을 가져오려고 한다면 route를 써야한다. 
            this.selectedNums = _.sampleSize(numbers,this.$route.params.lottoNum)
        }
    }

}
</script>

<style>

</style>