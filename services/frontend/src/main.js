import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from "vue";
import axios from 'axios';

import App from './App.vue';
import router from './router';
import store from './store';

import ViewUIPlus from 'view-ui-plus'
import 'view-ui-plus/dist/styles/viewuiplus.css'

//Added!!!!!
import VueMarkdownEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';
import '@kangc/v-md-editor/lib/theme/style/vuepress.css';

import Prism from 'prismjs';

VueMarkdownEditor.use(vuepressTheme, {
  Prism,
});

const app = createApp(App);//.use(router).use(store);

axios.defaults.withCredentials = true;
//Changed!!! also in vue.config.js
axios.defaults.baseURL = 'http://39.105.206.55:82/';  // the FastAPI backend

/*
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
*/

app.use(router);
app.use(store);

app.use(ViewUIPlus);

app.use(VueMarkdownEditor);

app.mount("#app");
