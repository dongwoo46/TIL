<template>
  <div id="app">
    <h1>캐릭터 진화 단게 가이드</h1>
    <nav>
      <router-link :to="{name: 'Home'}">Home</router-link> |
      <router-link :to="{name: 'Happeed'}">Start</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

i {
  font-size: xx-large;
}
img {
  width: 200px
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.wrap {
  
}
</style>
