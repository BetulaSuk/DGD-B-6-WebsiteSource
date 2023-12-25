<style>

.word {
  font-family:'Courier New', Courier, monospace;
  font-size: 20px;
  font-weight: bold;
  text-align: center;
}

.demo-carousel {
  background-color: azure;
  font-size: large;
}

.label {
  font-weight: bold;
  font-size: 16px;
}


</style>

<template>
  <section class="word">
      <p>This site is built with FastAPI and Vue.</p>
      <p>Something to say</p>
  </section>

  <div style="display: flex;">
    <div style="flex: 1;"></div>
    <div style="flex: 4;">
      <br />
      <br />
      <p class="label">TODO 1</p>
      <Progress :percent="45" :stroke-width="30" status="normal" text-inside />
      <br />
      <br />
      <p class="label">TODO 2</p>
      <Progress :percent="80" :stroke-width="30" status="active" text-inside />
      <br />
      <br />
      <p class="label">TODO 3</p>
      <Progress :percent="100" :stroke-width="30" text-inside />
    </div>
    <div style="flex: 1;"></div>
  </div>

</template>
<script>

export default {
  data () {
    return {}
  }
}


</script>

<!--
<template>
  <section>
    <p>This site is built with FastAPI and Vue.</p>

    <div v-if="isLoggedIn" id="logout">
      <p id="logout">Click <a href="/dashboard">here</a> to view all notes.</p>
    </div>
    <p v-else>
      <span><a href="/register">Register</a></span>
      <span> or </span>
      <span><a href="/login">Log In</a></span>
    </p>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
export default defineComponent({
  name: 'HomeView',
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
});
</script>
-->