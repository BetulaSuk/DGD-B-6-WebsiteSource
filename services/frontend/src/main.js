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
axios.defaults.baseURL = 'http://localhost:82/';  // the FastAPI backend

app.use(router);
app.use(store);

app.use(ViewUIPlus)

app.mount("#app");
