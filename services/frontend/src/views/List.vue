<style>
.page_container {
    display: block;
}

.grid {
    margin: 4em;
}

.words {
    margin: 2em;
    font-family:'Courier New', Courier, monospace;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
}


</style>



<template>
    <div class="page_container">
        <p class="words">The Results:</p>
        <Grid class="grid" col=4 square hover center>
            <GridItem>
                <Button @click="value1 = true" type="primary">View information1</Button>
                <Drawer :closable="false" width="640" v-model="value1">
                    <p class="words">Some information1</p>
                </Drawer>
            </GridItem>
            <GridItem>
                <Button @click="value2 = true" type="primary">View information2</Button>
                <Drawer :closable="false" width="640" v-model="value2">
                    <p class="words">Some information2</p>
                </Drawer>
            </GridItem>
            <GridItem>
                <!--TODO-->
                <ListComponent></ListComponent>
            </GridItem>
            <GridItem>4</GridItem>
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
        return {
            value1: false,
            value2: false,
        };
    },
}
</script>