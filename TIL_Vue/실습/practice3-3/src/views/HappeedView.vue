<template>
    <div>
        <h2>시작</h2>
        <img src="../assets/happeed.png" alt="">
        <h2>해피드</h2>
        <button @click="toHome"></button>
        <button @click="toHappling"></button>
    </div>
</template>

<script>
export default {
    name: 'HappeedView',
    methods: {
        toHome() {
            this.$router.push({name: 'Home'})

        },
        toHappling() {
            this.$router.push({name: 'Happling'})
        }
    }
}
</script>

<style>
img {
    width:50%;
    height:auto;
}
</style>