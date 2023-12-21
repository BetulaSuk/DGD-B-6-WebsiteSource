import axios from 'axios';

const actions = {
    async search_by_title({}, key) {
        /*
        await axios.post("search", {
            "keyword": key,
            "data_type": "pdf_data",
            "method": "title"
        });
        */
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
    }
}

export default {
    namespace: true,
    actions
};