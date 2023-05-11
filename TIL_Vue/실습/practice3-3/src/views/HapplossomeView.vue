<template>
    <div>
        <h2>시작</h2>
        <img src="../assets/happlossome.png" alt="">
        <h2>해플라썸</h2>
        <button @click="toHappling"></button>
        <button @click="toHapplower"></button>
    </div>
</template>

<script>
export default {
    name: 'HappeedView',
    methods: {
        moveLeft() {
            alert('이전단계로 돌아갈수 없어')
        },
        moveRight() {
            this.$router.push()
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