<template>
  <div id="app" class="wrapper">
    <div class="header">
      <NavBar />
    </div>
    <div class="main container">
      <router-view/>
    </div>
    <div class="footer">
      <GlobalFooter />
    </div>
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

  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;

}
.main {
  padding-top: 5em;
  flex: 1;
}

.wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100%;
}

.header {
  flex: 0;
}
.footer {
  flex: 0;
}

</style>