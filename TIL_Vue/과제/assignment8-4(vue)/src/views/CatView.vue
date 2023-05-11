<template>
    <div>
        <h1>Cat Images</h1>
        <img v-if="imgSrc" :src="imgSrc" alt="">
        <button @click="getCat">Get Cat!</button>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'CatView',
    data() {
        return {
            imgSrc: null,
        }
    },
    methods: {
        getCat() {
            const id = this.$route.params.id
            const catImageSearchURL = `https://api.thecatapi.com/v1/images/search/${id}`
            // const breed = this.$route.params.breed

            axios({
                method : 'get',
                url : catImageSearchURL
            })
            .then((response) => {
                console.log(response)
            })
            .catch((error)=> {
                console.log(error)
            })
        }   
    },
    created() {
        this.getCat()
    }
}
</script>

<style>

</style>