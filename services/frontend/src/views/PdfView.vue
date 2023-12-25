<template>
    <p>{{ this.paper_id }}</p>
</template>

<script>
export default {
    data() {
        return {
            paper_id: String
        };
    },
    methods: {
        init() {
            this.paper_id = this.$route.params.id;
            //console.log(this.paper_id);
        }
    },
    mounted() {
        this.init();
    }
};
</script>