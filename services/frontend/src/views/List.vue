<style>
.page_container {
    display: block;
}

.grid {
    margin: 1em;
}

.words {
    font-family:'Courier New', Courier, monospace;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
}

.title {
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    color: #464c5b;
    height: 6em;
}

.year {
    font-size: 16px;
    text-align: center;
    color: #464c5b;
}

.author {
    margin: 2em;
    color: #657180;
    font-size: 14px;
}

.abstract {
    margin: 2em;
    color: #0e73ed;
    font-size: 14px;
}


</style>

<template>
    <div class="page_container">
        <div ref="scroll" v-scroll="handleScroll" style="height: 660px; overflow: auto;">
            <Grid class="grid" col=4 square hover>
                <div v-for="(paper, index) in result" :key="paper">
                    <GridItem>
                        <Divider style="color: #2db7f5; font-weight: bold;">Title</Divider>
                        <p class="title">{{ paper.title }}</p>
                        <Divider style="color: #2db7f5; font-weight: bold;">Year</Divider>
                        <p class="year">{{ paper.year }}</p>
                        <Divider />
                        <div style="display: flex;">
                            <div style="flex: 1"></div>
                            <Button @click="valueList[index] = true" type="info" icon="md-book" style="width: 16em;">View More</Button>
                            <div style="flex: 1"></div>
                        </div>
                        <Drawer :closable="false" width="1000" v-model="valueList[index]">
                            <Divider style="font-weight: bold;">Authors</Divider>
                            <p class="author">{{ paper.author_name }}</p>
                            <Divider style="font-weight: bold;">Abstract</Divider>
                            <p class="abstract">{{ paper.abstract }}</p>
                            <!--TODO-->

                        </Drawer>
                    </GridItem>
                </div>
            </Grid>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            result: Array,
            valueList: Array
        };
    },
    methods: {
        init() {
            const data = this.$store.state.search.data;
            //this.result = JSON.parse(data);
            this.result = data["data"];
            console.log(this.result);

            this.valueList = [];
            //for(const i in this.result) {
            //    this.valueList.push(false);
            //}
        },
        handleScroll(event) {
            const container = this.$refs.scroll;
            const deltaY = event.deltaY;
            container.scrollTop += deltaY;
        }
    },
    mounted() {
        this.init();
    },
};
</script>