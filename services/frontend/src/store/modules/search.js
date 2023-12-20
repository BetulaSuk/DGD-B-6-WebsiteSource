import axios from 'axios';
import { toRaw } from "@vue/reactivity"

const text = {
    search_text: null,
}


const actions = {
    async search_by_title({}, key) {
        console.log('test haha');
        //这里的post还有问题
        console.log(key);
        await axios.post("search", {
            'data_type': 'pdf_data',
            'method': 'title',
            'keyword': key
        });
        //console.log(toRaw(key));
        //await dispatch('what');
    }
}

export default {
    namespace: true,
    text,
    actions
};