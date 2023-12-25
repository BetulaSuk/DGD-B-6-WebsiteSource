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
        <p class="title">Log In</p>
        <br/><br/>
        <!--<form @submit.prevent="submit">-->
        <form>
          <div class="mb-3">
            <label for="username" class="form-label">Username:</label>
            <input type="text" name="username" v-model="form.username" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password:</label>
            <input type="password" name="password" v-model="form.password" class="form-control" />
          </div>
          <br />
          <br />
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
  name: 'LoginView',
  data() {
    return {
      form: {
        username: '',
        password:'',
      }
    };
  },
  methods: {
    ...mapActions(['logIn']),
    async submit() {
      const User = new FormData();
      User.append('username', this.form.username);
      User.append('password', this.form.password);
      
      await this.logIn(User);
      //this.$router.push('/dashboard');
    }
  }
});
</script>