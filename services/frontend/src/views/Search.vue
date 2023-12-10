<template>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <Space direction="vertical" size="large" type="flex">
        <Input type="text" name="searchText" v-model="searchText" search enter-button clearable placeholder="Enter something..." />
    </Space>
</template>


<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
    name: 'Search',
    data() {
        return {
            searchText: '',
        };
    },
    methods: {
        ...mapActions('search', ['search']),
        async submit() {
            const Search = new FormData();
            Search.append('searchText', this.searchText);
            await this.search(Search);
            this.$router.push('/');
        }
    }
});
</script>