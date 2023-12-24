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


</style>

<template>
  <section class="word">
      <p>This site is built with FastAPI and Vue.</p>
    <p>
      <span><a href="/search">Search page</a></span>
      <span> or </span>
      <span><a href="/list">List page</a></span>
    </p>
  </section>

  <Carousel v-model="value">
        <CarouselItem>
            <div class="demo-carousel">
              <Grid center square hover>
                <GridItem>Something1</GridItem>
                <GridItem>Something2</GridItem>
                <GridItem>Whatever</GridItem>
              </Grid>
            </div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel">
              <Grid center square hover>
                <GridItem>Something1</GridItem>
                <GridItem>Something2</GridItem>
                <GridItem>Whatever</GridItem>
              </Grid>
            </div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel">
              <Grid center square hover>
                <GridItem>Something1</GridItem>
                <GridItem>Something2</GridItem>
                <GridItem>Whatever</GridItem>
              </Grid>
            </div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel">
              <Grid center square hover>
                <GridItem>Something1</GridItem>
                <GridItem>Something2</GridItem>
                <GridItem>Whatever</GridItem>
              </Grid>
            </div>
        </CarouselItem>
  </Carousel>

</template>
<script>

export default {
  data () {
    return {
      value: 0
    }
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