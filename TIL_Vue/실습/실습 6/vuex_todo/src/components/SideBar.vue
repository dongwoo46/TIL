<template>
  <div id="nav">
    <!-- 실제 페이지 이동을 막기 위해 .prevent 사용 -->
    <a href="" @click.prevent="changeComponent('all')" :class="{select: currentClassStatus.selectedAll}">모든</a>
    <a href="" @click.prevent="changeComponent('today')" :class="{select: currentClassStatus.selectedToday}">오늘</a>
    <a href="" @click.prevent="changeComponent('important')" :class="{select: currentClassStatus.selectedImportant}">중요</a>
  </div>
</template>

<script>

export default {
  name: 'SideBar',
  methods: {
    changeComponent (selected) {
      // 선택한 링크 전달
      this.$emit('select-component', selected)
      // 클릭한 링크 색을 변경
      this.$store.dispatch('changeClassStatus', selected)
    }
  },
  computed: {
    currentClassStatus () {
      return this.$store.getters.currentClassStatus
    }
  }

}
</script>

<style scoped>
#nav {
  border-radius: .5rem;
  border: 2px solid #2c3e50;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
}

#nav a {
  text-decoration: none;
  color: #2c3e50;
  font-size: 2rem;
}

#nav a.select {
  color: #42b983;
}
</style>