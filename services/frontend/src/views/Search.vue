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
    <form @submit.prevent="submit">
    <Space direction="vertical" size="large" type="flex">
        <Input type="text" name="search_text" v-model="searchText" search enter-button  clearable placeholder="Enter something..." />
        <button @click="submit()">search</button>
    </Space>
    </form>
</template>


<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
    name: 'Search',
    data() {
        return {
            form: {
                searchText: '',
            }
        };
    },
    methods: {
        ...mapActions(['search']),
        async submit() {
            const Search = new FormData();
            Search.append('searchText', this.form.searchText);
            await this.search(Search);
            this.$router.push('/');
        }
    }
});
</script>