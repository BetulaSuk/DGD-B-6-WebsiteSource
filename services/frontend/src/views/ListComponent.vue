<template>
    <p class="words">{{ paper_title }}</p>
    <Button @click="value1 = true" type="primary">Abstract</Button>
    <Drawer :closable="false" width="640" v-model="value1">
        <p class="words">{{ paper_abstract }}</p>
    </Drawer>
    <br> <!--TODO-->
    <Button @click="value2 = true" type="primary">Authors</Button>
    <Drawer :closable="false" width="640" v-model="value2">
        <p class="words">{{ paper_authors }}</p>
    </Drawer>
</template>

<script>
export default {
    data() {
        return {
            value1: false,
            value2: false
        };
    },
    methods: {
        fetchInfo() {
            const data = this.$route.query.data;
            const result = JSON.parse(data);
            console.log("result is:");
            console.log(result);
            this.paper_title = result[0]["title"];
            this.paper_abstract = result[0]["abstract"];
            this.paper_authors = result[0]["author_name"];
        }
    },
    created() {
        this.fetchInfo();
    },
};
</script>