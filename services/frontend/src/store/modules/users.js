import router from '@/router';
import axios from 'axios';

const state = {
  user: null,
};

const getters = {
  isAuthenticated: state => !!state.user,
  stateUser: state => state.user,
};

const actions = {
  async register({dispatch}, form) {
    await axios.post('register', form);
    let UserForm = new FormData();
    UserForm.append('username', form.username);
    UserForm.append('password', form.password);
    await dispatch('logIn', UserForm);
  },
  async logIn({dispatch}, user) {
    await axios.post('login', user)
      .then(response => {
        console.log(response);
        dispatch('viewMe');
      })
      .catch(error => {
        console.log('Exists error');
        console.log(error);
        alert('Try Again');
      });
    //await dispatch('viewMe');
  },
  async viewMe({commit}) {
    let {data} = await axios.get('users/whoami');
    //console.log(data);
    await commit('setUser', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteUser({}, id) {
    await axios.delete(`user/${id}`);
  },
  async logOut({commit}) {
    let user = null;
    commit('logout', user);
  }
};

const mutations = {
  setUser(state, username) {
    state.user = username;

    //console.log('setUser succeeded');
    router.push('/dashboard');

  },
  logout(state, user){
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};