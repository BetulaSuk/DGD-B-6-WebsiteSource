<style>
.page_container {
    display: block;
}

.grid {
    margin: 1em;
}

.words {
    margin: 1em;
    font-family:'Courier New', Courier, monospace;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
}

</style>

<template>
    <div class="page_container">
        <p class="words">The Results:</p>
        <Grid class="grid" col=3 square hover center>
            <GridItem>
                <ListComponent />
            </GridItem>
            <GridItem>
                <ListComponent />
            </GridItem>
            <GridItem>
                <ListComponent />
            </GridItem>
        </Grid>
        <div style="display: flex">
            <div style="flex: 1"></div>
            <Page :total="10" show-total />
            <div style="flex: 1"></div>
        </div>
    </div>
</template>

<script>
import ListComponent from './ListComponent.vue'
export default {
    data() {
        return {};
    },
    components: {
        ListComponent,
    },
};
</script>