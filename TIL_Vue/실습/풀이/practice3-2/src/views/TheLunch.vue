<template>
    <div>
        <h1>점심메뉴</h1>
        <button @click="pickOneLunchMenu">Pick Menu</button>
        <p>{{selectedMenu}}</p>
        <br>
        <h2>로또를 뽑아보자!</h2>
        <button @click="pickLottoNum">Pick Lotto</button>
    </div>
</template>

<script>
import _ from 'lodash'
export default {
    name: 'TheLunch',
    data() {
        return {
            lunch : ['사과','치킨','복숭아', '햄버거', '개고기'],
            selectedMenu : null,
        }
    },
    methods: {
        pickOneLunchMenu() {
            this.selectedMenu = _.sample(this.lunch)
        },
        pickLottoNum() {
            // 전체에서 가져올 때는 router를 사용해야한다. 
            this.$router.push({name:'TheLotto', params:{lottoNum:6}})
        }
    }
}
</script>

<style>

</style>