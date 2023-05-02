<template>
  <div id="app">
    <h1>캐릭터 진화 단계 가이드</h1>
    <div class="button-container">
      <div @click="clickHome" class="aTag">
        <button>Home</button>
      </div>
      <div @click="clickStart" class="aTag">
        <button>Start</button>
      </div>
    </div>
    <div v-if="!isStarted">
      <h2>Start 버튼으로 시작해보세요</h2>
      <img src="./assets/ssafy-banner.png" alt="SSAFY"> 
    </div>
    <div v-else>
      <div @click="clickLeft" class='arrow arrow--left'></div>
      <SsanoColor v-if="page===1"/>
      <SsaFling v-if="page===2"/>
      <SsafLeaf v-if="page===3"/>
      <SsaFlower v-if="page===4"/>
      <div class="parent">
        <div @click="clickRight" class="arrow arrow--right"></div>
      </div>

    </div>

  </div>
</template>

<script>
import SsanoColor from './components/SsanoColor.vue'
import SsafLeaf from './components/SsafLeaf.vue'
import SsaFling from './components/SsaFling.vue'
import SsaFlower from './components/SsaFlower.vue'


export default {
  name: 'App',
  components: {
    SsanoColor,
    SsafLeaf,
    SsaFling,
    SsaFlower,
    // Home,
    // Ssafleaf,
    // Ssafling,
    // Ssaflower,
  },
  data:function() {
    return {
      page: 1,
      isStarted: false,
    }
  },
  methods: {
    clickHome() {
      this.isStarted = false
      this.page=1
    },
    clickStart() {
      this.isStarted = true
      this.page=1
    },
    clickLeft() {
      if (this.page===1){
        this.isStarted = false
      } else {
        this.page --
      }
    },
    clickRight() {
      if (this.page===4){
        alert('Home으로 돌아가용~')
        this.page = 1
        this.isStarted = false
      } else {
        this.page ++
      }
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

.aTag {
  cursor:pointer;
}

.arrow{
  width:32px;
  height:32px;
  position:relative;
  margin-bottom:30px;
}

.arrow::before, .arrow::after{
  content:"";
  position: absolute;
}
.arrow::before{
  width:100%;
  height:100%;
  border:1px solid black;
  border-right:0;
  border-bottom:0;
}
.arrow::after{
  width:48px;
  height:1px;
  background:black;
  transform-origin: 0 100%;
  transform: rotate(45deg);
}
.arrow--left {
  transform: rotate(-45deg);
}
.arrow--right {
  transform:rotate(135deg);
}
.parent {
  display:flex;
  justify-content: flex-end;
}
img {
  width: 400px;
  height: 400px;
}
.button-container {
  text-align: center;
}

.button-container > div {
  display: inline-block;
  margin: 0 10px;
}
</style>
