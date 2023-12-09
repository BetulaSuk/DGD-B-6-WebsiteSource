<style scoped>
    .layout{
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
    }
    .layout-header-bar{
        background: #fff;
        box-shadow: 0 1px 1px rgba(0,0,0,.1);
    }
    .menu-item span{
        display: inline-block;
        overflow: hidden;
        width: 69px;
        text-overflow: ellipsis;
        white-space: nowrap;
        vertical-align: bottom;
        transition: width .2s ease .2s;
    }
    .menu-item i{
        transform: translateX(0px);
        transition: font-size .2s ease, transform .2s ease;
        vertical-align: middle;
        font-size: 16px;
    }
    .collapsed-menu span{
        width: 0px;
        transition: width .2s ease;
    }
    .collapsed-menu i{
        transform: translateX(5px);
        transition: font-size .2s ease .2s, transform .2s ease .2s;
        vertical-align: middle;
        font-size: 22px;
    }
    .dev-run-preview .dev-run-preview-edit{ display: none }
</style>

<template>
    <div class="layout">
        <Layout>
            <Sider breakpoint="md" collapsible :collapsed-width="78" v-model="isCollapsed">
                <Menu active-name="1-2" theme="dark" width="auto" :class="menuitemClasses">
                    <MenuItem name="1-1">
                        <Icon type="ios-document-outline"></Icon>
                        <span>Paper 1</span>
                    </MenuItem>
                    <MenuItem name="1-2">
                        <Icon type="ios-document-outline"></Icon>
                        <span>Paper 2</span>
                    </MenuItem>
                    <MenuItem name="1-3">
                        <Icon type="ios-document-outline"></Icon>
                        <span>Paper 3</span>
                    </MenuItem>
                </Menu>
                <div #trigger></div>
            </Sider>
            <Layout>
                <Header class="layout-header-bar"></Header>
                <Scroll>
                    <Card dis-hover v-for="(item, index) in list" :key="index" style="margin: 32px 0">
                        Content {{ item }}
                    </Card>
                </Scroll>
            </Layout>
        </Layout>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                isCollapsed: false,
                list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            };
        },
        computed: {
            menuitemClasses: function () {
                return [
                    'menu-item',
                    this.isCollapsed ? 'collapsed-menu' : ''
                ]
            }
        }
    }
</script>