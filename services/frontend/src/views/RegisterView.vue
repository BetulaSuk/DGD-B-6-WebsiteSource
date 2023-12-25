<style>

.title {
  margin: 1em;
  text-align: center;
  font-size: 32px;
  font-weight: bold;
}

.form-label {
  margin: 1em;
  font-size: 16px;
  font-weight: bold;
}

</style>


<template>
  <section>
    <div style="display: flex;">
      <div style="flex: 1;"></div>
      <div style="flex: 1;">
        <p class="title">Register</p>
        <!--<form @submit.prevent="submit">-->
        <form>
          <div class="mb-3">
            <label for="username" class="form-label">Username:</label>
            <input type="text" name="username" v-model="user.username" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="full_name" class="form-label">Full Name:</label>
            <input type="text" name="full_name" v-model="user.full_name" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password:</label>
            <input type="password" name="password" v-model="user.password" class="form-control" />
          </div>
          <Button @click="submit" type="success" long>SUBMIT</Button>
        </form>
      </div>
      <div style="flex: 1;"></div>
    </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
  name: 'RegisterView',
  data() {
    return {
      user: {
        username: '',
        full_name: '',
        password: '',
      },
    };
  },
  methods: {
    ...mapActions(['register']),
    async submit() {
      try {
        await this.register(this.user);
        this.$router.push('/dashboard');
      } catch (error) {
        throw 'Username already exists. Please try again.';
      }
    },
  },
});
</script>