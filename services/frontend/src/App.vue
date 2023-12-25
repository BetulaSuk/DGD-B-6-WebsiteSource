<template>
  <div id="app" class="wrapper">
    <div class="header">
      <NavBar />
    </div>
    <div class="main">
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


export default {
  components: {
    NavBar,
    GlobalFooter,
  },
  //解决ListView界面刷新会丢失vuex数据的问题
  created() {
    if (sessionStorage.getItem('store')) {
      this.$store.replaceState(Object.assign({}, this.$store.state, JSON.parse(sessionStorage.getItem("store"))))
    }
    window.addEventListener("beforeunload", () => {
      sessionStorage.setItem('store', JSON.stringify(this.$store.state))
    })
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
  padding-top: 1em;
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