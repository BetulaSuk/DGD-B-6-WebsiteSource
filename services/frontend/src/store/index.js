import { createStore } from "vuex";

import notes from './modules/notes';
import users from './modules/users';
import search from './modules/search';

export default createStore({
  modules: {
    notes,
    users,
    search,
  }
});