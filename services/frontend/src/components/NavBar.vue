<style>

.logIn {
  color: blueviolet;
}

</style>


<template>
    <header>
      <nav class="navbar navbar-expand-md navbar-dark bg-dark">
        <div class="container">
          <a ref="brand" class="navbar-brand" href="/">Our Website</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">\
            <ul class="navbar-nav me-auto mb-2 mb-md-0">
              <li class="nav-item">
                <router-link class="nav-link" to="/search">Search</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/dashboard">Dashboard</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/login">Log in</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/register">Register</router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'NavBar',
    computed: {
      isLoggedIn: function() {
        return this.$store.getters.isAuthenticated;
      }
    },
    methods: {
      async logout () {
        await this.$store.dispatch('logOut');
        this.$router.push('/login');
      }
    },
    mounted() {
      if (this.$store.getters.isAuthenticated) {
        this.$refs.brand.classList.add('logIn');
      }
    }
  });
  </script>
  
  <style scoped>
  a {
    cursor: pointer;
  }
  </style>