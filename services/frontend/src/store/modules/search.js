import axios from 'axios';
import { toRaw } from "@vue/reactivity"

const text = {
    search_text: null,
}


const actions = {
    async search({dispatch}, form) {
        console.log('test haha');
        //这里的post还有问题
        //await axios.post("search", form);
        console.log(toRaw(form));
        //await dispatch('what');
    }
}

export default {
    namespace: true,
    text,
    actions
};