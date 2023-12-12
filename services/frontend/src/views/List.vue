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

.demo-drawer-profile{
        font-size: 14px;
    }
.demo-drawer-profile .ivu-col{
    margin-bottom: 12px;
}
</style>



<template>
    <div class="page_container">
        <p class="words">The Results:</p>
        <Grid class="grid" col=4 square hover center>
            <GridItem>
                <Button @click="value = true" type="primary">View Profile</Button>
                <Drawer :closable="false" width="640" v-model="value">
                    <p class="words">Some information</p>
                </Drawer>
            </GridItem>
            <GridItem>2</GridItem>
            <GridItem>3</GridItem>
            <GridItem>4</GridItem>
        </Grid>
        <div style="display: flex">
            <div style="flex: 1"></div>
            <Page :total="x" show-total />
            <div style="flex: 1"></div>
        </div>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                value: false,
            };
        },
    }
</script>