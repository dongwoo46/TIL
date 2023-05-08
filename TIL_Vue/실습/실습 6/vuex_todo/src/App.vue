<template>
  <div id="app">
    <SideBar @select-component="changeComponent"/>
    <div id="main">
      <!-- component 태그에서 is 속성에 components 에 등록된 .vue 를 넣으면 해당 컴포넌트가 화면에 나타남 -->
      <component :is="currentComponent"></component>
    </div>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'
import AllTodoPage from '@/components/AllTodoPage'
import TodayTodoPage from '@/components/TodayTodoPage'
import ImportantTodoPage from '@/components/ImportantTodoPage'

export default {
  name: 'App',
  components: {
    SideBar,
    AllTodoPage,
    TodayTodoPage,
    ImportantTodoPage,
  },
  methods: {
    // 컴포넌트를 변경하기 위한 메서드
    changeComponent (component) {
      this.$store.dispatch('changeComponent', component)
    }
  },
  computed: {
    currentComponent () {
      return this.$store.getters.currentComponent
    }
  },

}
</script>

<style>
#app {
  color: #2c3e50;
  height: 100vh;
  display: flex;
  column-gap: 1rem;
  padding: 3rem;
}

#main {
  border-radius: .5rem;
  border: 2px solid #2c3e50;
  width: 100%;
  padding: 2rem 1.25rem;
}

#nav {
  width: 200px;
}
</style>
