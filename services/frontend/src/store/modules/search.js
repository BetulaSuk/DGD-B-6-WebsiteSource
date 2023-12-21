import axios from 'axios';

const state = {
    data: null
};

const getters = {
    stateData: state => state.data
};

const actions = {
    async search_by_title({dispatch}, key) {
        /*
        const response = await fetch("http://localhost:82/search", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "keyword": key,
                "data_type": "pdf_data",
                "method": "title"
            })
        });
        return response;
        */
        const response = await axios.post('search', {
                "keyword": key,
                "data_type": "pdf_data",
                "method": "title"
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