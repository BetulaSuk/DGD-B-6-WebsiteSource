import axios from 'axios';

const state = {
    data: null,
    keyword: null
};

const getters = {
    stateData: state => state.data
};

const actions = {
    async search_by_title({dispatch}, para) {
        //console.log(para);
        const response = await axios.post('search', {
                "keyword": para[0],
                "data_type": para[2],
                "method": para[1]
            });
        //console.log(response);
        await dispatch('getData', response);
    },
    async getData({commit}, response) {
        commit('setData', response); 
    },
    async getKeyWord({commit}, keyword) {
        commit('setKeyWord', keyword);
    }
};

const mutations = {
    setData(state, newData) {
        state.data = newData;
    },
    setKeyWord(state, newKey) {
        state.keyword = newKey;
    }
};

export default {
    //namespace: true,
    state,
    getters,
    actions,
    mutations
};