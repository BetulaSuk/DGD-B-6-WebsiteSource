import axios from 'axios';

const text = {
    search_text: null,
}


const actions = {
    async search(text) {
        const response = await axios.post("backend_url/search", text);
        console.log(response.data);
    }
}

export default {
    text,
    actions
};