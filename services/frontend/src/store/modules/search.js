import axios from 'axios';
import { toRaw } from "@vue/reactivity"

const text = {
    search_text: null,
}


const actions = {
<<<<<<< HEAD
    async search({dispatch}, form) {
        console.log('test haha');
        //这里的post还有问题
        //await axios.post("search", form);
        console.log(toRaw(form));
        //await dispatch('what');
=======
    async search(text) {
        const response = await axios.post("search", text);
        console.log(response.data);
>>>>>>> ee10df0 (partly job for combination)
    }
}

export default {
    namespace: true,
    text,
    actions
};