<style>

.words {
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
  <section class="words">
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