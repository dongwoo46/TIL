<template>
  <div id="app">
    <SideBar/>
    <main>
      <router-view/>
    </main>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar'

export default ({
  components: {
    SideBar
  },
})
</script>

<style>
#app {
  color :#2c3e50;
  height: 100vh;
  display:flex;
  padding: 3rem;
  column-gap: 1rem;
  /* 컬럼 설정하고 비율을 나누는 것 */
  grid-template-columns: 1fr 4fr;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  
}

/* nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
} */

main {
  border: 2px solid #2c3e50;
  border-radius: .5rem;
  padding: 2rem 1.25rem;
}
</style>
