<template>
    <div>
        <h2>시작</h2>
        <img src="../assets/happling.png" alt="">
        <h2>해플링</h2>
        <button @click="moveLeft"></button>
        <button @click="moveRight"></button>
    </div>
</template>

<script>
export default {
    name: 'HapplingView',
    methods: {
        toHappeed() {
            this.$router.push({name: 'Happeed'})
        },
        toHapplossome() {
            this.$router.push({name: 'Happlossome'})
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