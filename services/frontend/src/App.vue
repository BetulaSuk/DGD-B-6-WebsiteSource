<template>
  <div id="app">
    <NavBar />
    <div class="main container">
      <router-view/>
    </div>
    <GlobalFooter />
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar.vue'
import GlobalFooter from '@/components/GlobalFooter.vue';
import Search from './views/Search.vue';

export default {
  components: {
    NavBar,
    GlobalFooter,
    Search
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.main {
  padding-top: 5em;
}
</style>