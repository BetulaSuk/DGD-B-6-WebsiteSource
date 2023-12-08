<template>
  <section>
      <b-button @click="clickMe">Click Me</b-button>
  </section>
  <Space direction="vertical" size="large" type="flex">
      <Input search placeholder="Enter something..." />
      <Input search enter-button placeholder="Enter something..." />
      <Input search enter-button="Search" placeholder="Enter something..." />
  </Space>
</template>

<script>
  export default {
      methods: {
          clickMe() {
              this.$buefy.notification.open('Clicked!!')
          }
      }
  }
</script>