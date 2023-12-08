<template>
  <section>
    <p>This site is built with FastAPI and Vue.</p>
    <p>What should we put here?</p>

    <!--
    <div v-if="isLoggedIn" id="logout">
      <p id="logout">Click <a href="/dashboard">here</a> to view all notes.</p>
    </div>
    -->
    <p>
      <span><a href="/search">Search page</a></span>
      <span> or </span>
      <span><a href="/list">Some interesting pages</a></span>
    </p>
  </section>

  <Carousel v-model="value" loop>
        <CarouselItem>
            <div class="demo-carousel">
              <Grid center square>
                <GridItem>Something1</GridItem>
                <GridItem>Something2</GridItem>
                <GridItem>Whatever</GridItem>
              </Grid>
            </div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel">
              <Grid center square>
                <GridItem>Something1</GridItem>
                <GridItem>Something2</GridItem>
              </Grid>
            </div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel">
              <h1> 11111 </h1>
            </div>
        </CarouselItem>
        <CarouselItem>
            <div class="demo-carousel">
              <h1> 11111 </h1>
            </div>
        </CarouselItem>
  </Carousel>

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