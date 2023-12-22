import axios from 'axios';

const state = {
    data: null
};

const getters = {
    stateData: state => state.data
};

const actions = {
    async search_by_title({dispatch}, meth, key) {
        console.log(key);
        console.log(meth);
        const response = await axios.post('search', {
                "keyword": key,
                "data_type": "pdf_data",
                "method": "title",
            });
	    console.log(response);
        await dispatch('getData', response);
    },
    async getData({commit}, response) {
        commit('setData', response);
    }
};

const mutations = {
    setData(state, newData) {
        state.data = newData;
    }
};

export default {
    //namespace: true,
    state,
    getters,
    actions,
    mutations
};