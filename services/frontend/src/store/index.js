import { createStore } from "vuex";

import notes from './modules/notes';
import users from './modules/users';
import search from './modules/search';
import pdf from './modules/pdf';

export default createStore({
  modules: {
    notes,
    users,
    search,
    pdf
  }
});