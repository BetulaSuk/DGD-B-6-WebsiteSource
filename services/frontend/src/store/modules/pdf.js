import axios from 'axios';

const state = {
    title: '',
    text: '',
    pdf_id: ''
};

const getters = {
    stateTitle: state => state.title,
    stateText: state => state.text,
    statePdf: state => state.pdf_id
};

const actions = {
    idSet({commit}, id) {
        commit('setId', id);
    },
    titleSet({commit}, title) {
        commit('setTitle', title);
    },
    textSet({commit}, text) {
        commit('setText', text);
    },
};

const mutations = {
    setId(state, id) {
        state.pdf_id = id;
    },
    setTitle(state, newTitle) {
        state.title = newTitle;
    },
    setText(state, newText) {
        state.text = newText;
    },
};

export default {
    //namespace: true,
    state,
    getters,
    actions,
    mutations
};