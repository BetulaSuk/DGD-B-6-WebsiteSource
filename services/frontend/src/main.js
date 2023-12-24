import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from "vue";
import axios from 'axios';

import App from './App.vue';
import router from './router';
import store from './store';

import ViewUIPlus from 'view-ui-plus'
import 'view-ui-plus/dist/styles/viewuiplus.css'

const app = createApp(App).use(router).use(store);

axios.defaults.withCredentials = true;
//Changed!!! also in vue.config.js
axios.defaults.baseURL = '/proxy_url';  // the FastAPI backend

axios.interceptors.response.use(undefined, function (error) {
    if (error) {
      const originalRequest = error.config;
      if (error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;
        store.dispatch('logOut');
        return router.push('/login');
      }
    }
  });

app.use(router);
app.use(store);

app.use(ViewUIPlus);

app.mount("#app");
