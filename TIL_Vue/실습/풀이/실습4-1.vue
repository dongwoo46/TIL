<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div class='container'>
      <h2>예약 페이지</h2>
      <br>
      <h3>시간 선택</h3>
      
      <section class="wrap">
      <div class='time-wrap'>
        <div class='timebox'>
          <span v-for="(time,index) in times" :key="index"><button class="timebtn" :class="{selected:selectedIndex===index}" @click="btnClick(index)">{{time}}</button></span>
        </div>
        <hr style="border: solid 1px blue;">
        <p v-for="(time,index) in selectedTime" :key="index">{{time}}</p>
      </div>
      </section>

    </div>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
  },
  data () {
    return {
      times: [
    "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
    "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
    "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
    ],
      selectedTime : [],
      selectedIndex : -1,
    }
  },
  methods: {
    btnClick (index) {
      this.selectedIndex = index;
      this.selectedTime.push({time:this.times[index]});
      if (this.selectedTime.length>5){
        alert('5타임까지만 신청할수 있습니다.')
      }
    },     
  }
}
</script>

<style>

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 700px;
  margin: 0 auto;
  border: solid;
  box-shadow: 0px 2px 2px 2px silver;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.timebox {
  width: 530px;
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 20px;
  align-content: center;
  justify-content: space-between;
}

.timebtn {
  background-color: white;
  border: transparent;
  color: silver;
  font-size: 16px; 
}

.selected{
  color:blue;
  background-color: skyblue;
}


</style>
