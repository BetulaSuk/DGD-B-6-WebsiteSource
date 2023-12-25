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

.title1 {
    font-size: 16px;
    /*font-weight: bold;*/
    text-align: center;
    color: #464c5b;
    height: 76px;

    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
}

.title2 {
    margin: 1em;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    color: #464c5b;
}

.year {
    font-size: 16px;
    text-align: center;
    color: #464c5b;
}

.author {
    margin: 2em;
    color: #464c5b;
    font-size: 14px;
}

.abstract {
    margin: 2em;
    color: #464c5b;
    font-size: 14px;
}

.keyword {
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    color: #f21a1a;
    height: 8em;
}


</style>

<template>
    <div class="page_container" style="display: flex;">
        <div style="flex: 1;">
            <Menu mode="horizontal" :theme="light" active-name="1">
                <MenuItem name="1">
                    <Icon type="ios-paper" />
                    Whatever1
                </MenuItem>
                <MenuItem name="2">
                    <Icon type="ios-people" />
                    Whatever2
                </MenuItem>
            </Menu>
        </div>
        <div ref="scroll" v-scroll="handleScroll" style="flex: 5; height: 660px; overflow: auto;">
            <Grid class="grid" col=4 square hover>
                <div v-for="(paper, index) in result" :key="paper">
                    <GridItem>
                        <Divider style="color: #2db7f5; font-weight: bold;">Title</Divider>
                        <p class="title1" v-html="highLightTitle(paper.title)"></p>

                        <Divider style="color: #2db7f5; font-weight: bold;">Year</Divider>
                        <p class="year">{{ paper.year }}</p>
                        <Divider />

                        <div style="display: flex;">
                            <div style="flex: 1"></div>
                            <Button @click="valueList[index] = true" type="info" icon="md-book" style="width: 16em;">View Details</Button>
                            <div style="flex: 1"></div>
                        </div>
                        <!--Detail Drawer-->
                        <Drawer :closable="false" width="1000" v-model="valueList[index]">
                            <p class="title2">{{ paper.title }}</p>
                            <div style="display: flex;">
                                <div style="flex: 1;">
                                    <Divider style="font-weight: bold;">Authors</Divider>
                                    <div class="author" v-for="author in paper.author_name">{{ author }}</div>
                                </div>
                                <div style="flex: 3;">
                                    <Divider style="font-weight: bold;">Abstract</Divider>
                                    <div ref="scroll" v-scroll="handleScroll" style="height: 360px; overflow: auto;">
                                        <p class="abstract">{{ paper.abstract }}</p>
                                    </div>
                                </div>
                            </div>
                            <!--TODO-->
                            <Divider style="font-weight: bold;">Pictures</Divider>
                            <Space wrap>
                                <template v-for="(url, index) in urlList" :key="url">
                                    <Image :src="url" fit="contain" width="120px" height="80px" preview :preview-list="urlList" :initial-index="index" />
                                </template>
                            </Space>
                            <Button @click="toNote(result[index].paper_id)" type="info" icon="md-book" style="width: 8em;">Take Notes</Button>
                        </Drawer>
                    </GridItem>
                </div>
            </Grid>
        </div>
    </div>
</template>

<script>

export default {
    name: 'ListView',
    data() {
        return {
            result: Array,
            valueList: Array,
            keyword: String,
            urlList: Array
        };
    },
    methods: {
        init() {
            const data = this.$store.state.search.data;
            this.keyword = this.$store.state.search.keyword;
            //this.result = JSON.parse(data);
            this.result = data["data"];
            //console.log(this.result);

            this.valueList = [];
            //TODO!!!!!
            this.urlList = [];
            //for(const i in this.result) {
            //    this.valueList.push(false);
            //}
        },
        handleScroll(event) {
            const container = this.$refs.scroll;
            const deltaY = event.deltaY;
            container.scrollTop += deltaY;
        },
        highLightTitle(text) {
            const _reg = new RegExp(this.keyword, "g");
            const rep = "<span class='keyword'>" + this.keyword + "</span>";
            const newText = text.replace(_reg, rep);
            return newText;
        },
        toNote(paper_id) {
            this.$router.push({
                name: 'PdfView',
                params: { id: paper_id }
            });
        }
    },
    mounted() {
        this.init();
    },
};
</script>