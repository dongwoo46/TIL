<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div class='container'>
        <section class="wrap">
            <div class='time-wrap'>
                <h2>예약 페이지</h2>
                <br>
                <h3>시간 선택</h3>

                <div class='timebox'>
                  <span class="timebtn" v-for="(time,index) in times" :key="index" @click="selectTime(time)" :class="{'selected-timebtn':isSelected(time)}">{{time}}</span>
                </div>
                <div class="divider">
                <div>
                <h3>선택 시간 : 
                  <span class="eachtime" v-for="(time,index) in selectedTimes" :key="index">{{time}}</span></h3>
              </div>
            </div>
            
              
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
      selectedTimes : [],
    }
  },
  methods: {
    selectTime (time) {
      if (this.selectedTimes.includes(time)){ // 삭제
        const time_idx = this.selectedTimes.indexOf(time)
        this.selectedTimes.splice(time_idx, 1)
      } else {
        if (this.selectedTimes.length ===5) { // 추가
          alert('5 타임까지만 추가할 수 있습니다.')
          return
        }
        this.selectedTimes.push(time)
      }
    },
    isSelected(time) {
      return this.selectedTimes.includes(time) ? true : false
    },
      // return this.selectedTimes.includes(time) ? true:false
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
.timebox {
  width: 530px;
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.timebtn {
  background-color: white;
  border: transparent;
  color: silver;
  font-size: 16px; 
  margin-bottom:20px;
  cursor:pointer;
  margin: 10px;
}

.time-wrap {
    display:flex;
    flex-direction: column;
    align-items: center;  
}

.wrap {
    display: flex;
    box-shadow: 0px 2px 4px 4px grey;
    width: 520px;
    margin: 0 auto;
}

.selected-timebtn {
  background-color: skyblue;
  color: blue;
}

.divider {
  border-top: 1px solid blue;
  width: 80%;
  margin-top: 20px;
}
.eachtime {
  margin: 5px;

}
</style>
