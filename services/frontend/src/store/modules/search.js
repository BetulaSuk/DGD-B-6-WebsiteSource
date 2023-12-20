import axios from 'axios';

const actions = {
    async search_by_title({}, key) {
        console.log('test haha');
        //这里的post还有问题
        console.log(key);
        await axios.post("search", {
            "keyword": key,
            "data_type": "pdf_data",
            "method": "title"
        });
    }
}

export default {
    namespace: true,
    actions
};