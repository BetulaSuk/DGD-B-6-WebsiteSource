<template>
    <h1>{{ paper_title }}</h1>
    <Button @click="value = true" type="primary">View information</Button>
    <Drawer :closable="false" width="640" v-model="value">
        <p class="words">{{ paper_info }}</p>
    </Drawer>
</template>

<script>
export default {
    data() {
        return {
            value: false,
        };
    },
    methods: {
        fetchInfo() {
            fetch('TODO')
                .then(response => response.json())
                .then(data => {
                    this.paper_title = data.paper_title;
                    this.paper_info = data.paper_info;
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    },
    mounted() {
        this.fetchInfo();
    },
};
</script>