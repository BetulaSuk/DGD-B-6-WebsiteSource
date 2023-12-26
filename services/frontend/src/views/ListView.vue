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

/*TODO*/

table {
    table-layout: auto;
    /*width: 400px;*/
    line-height: 1.2;
    text-align: center;
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
        <div ref="scroll" v-scroll="handleScroll" style="flex: 5; height: 80vh; overflow: auto;">
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
                            <div v-if="noTable == false">
                            <Divider style="font-weight: bold;">Table</Divider>
                            <table v-if="data.length > 0">
                                <thead>
                                <tr>
                                    <!--Error 12/26-->
                                    <th v-if="data[index]" v-for="(value, key) in data[index][0]" :key="key">{{ key }}</th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="row in data[index]">
                                    <td v-for="(value, key) in row" :key="key">{{ value }}</td>
                                </tr>
                                </tbody>
                            </table>
                            </div>
                            <!--TODO-->
                            <div v-if="noPic == false">
                            <Divider style="font-weight: bold;">Pictures</Divider>
                            <Space wrap>
                                    <Image :src="data2[2*index]" fit="contain" width="120px" height="80px" preview :preview-list="data2" :initial-index="2*index" />
                                    <Image :src="data2[2*index+1]" fit="contain" width="120px" height="80px" preview :preview-list="data2" :initial-index="2*index+1" />
                            </Space>
                            <br />
                            </div>
                            <Button @click="toNote(result[index].paper_id)" type="info" icon="md-book" style="width: 8em;">Take Notes</Button>
                        </Drawer>
                    </GridItem>
                </div>
            </Grid>
        </div>
    </div>
</template>

<script>
import Papa from 'papaparse';
import { mapActions } from 'vuex';
import axios from 'axios';

export default {
    name: 'ListView',
    data() {
        return {
            result: Array,
            valueList: Array,
            keyword: String,
            urlList: Array,
            data: Array,
            data2: Array,
            noTable: false,
            noPic: false,
        };
    },
    methods: {
        ...mapActions(['idSet']),
        init() {
            const data = this.$store.state.search.data;
            this.keyword = this.$store.state.search.keyword;
            //this.result = JSON.parse(data);
            this.result = data["data"];
            //console.log(this.result);

            this.valueList = [];
            //TODO!!!!!
            this.urlList = [];
            this.data = [];
            this.data2 = [];

            this.result.forEach(paper => {
                this.show(paper.paper_id);
            });

            this.result.forEach(paper => {
                this.getPic(paper.paper_id);
            })
            //console.log(this.data2);
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
        async toNote(paper_id) {
            await this.idSet(paper_id);
            this.$router.push('/pdf');
        },
        async show(id) {
            var url = 'http://localhost:82/static/100_PDF_results/'+ id + '/';
            await axios.get('/pdf/csv/' + id)
                .then(response => {
                    console.log(response.data);
                    url = url + response.data[0];
                })
                .catch(error => {
                    this.noTable = true;
                });
            const response = await fetch(url);
            const csvData = await response.text();
            console.log(csvData);
            Papa.parse(csvData, {
                header: true,
                dynamicTyping: true,
                complete: (result) => {
                    //console.log(result);
                    this.data.push(result.data);
                },
            })
        },
        async getPic(id) {
            var url1 = 'http://localhost:82/static/100_PDF_images/' + id + '/';
            var url2 = 'http://localhost:82/static/100_PDF_images/' + id + '/';
            await axios.get('/pdf/img/' + id)
                .then(response => {
                    console.log(response.data);
                    url1 = url1 + response.data[0];
                    url2 = url2 + response.data[1];
                })
                .catch(error => {
                    this.noPic = true;
                });;
            this.data2.push(url1);
            this.data2.push(url2);
        }
    },
    mounted() {
        this.init();
    },
};
</script>