<template>
    <GlobalFooter :links="links" :copyright="copyright" />
</template>

<script>
    export default {
        data () {
            return {
                links: [
                    {
                        key: '帮助',
                        title: '帮助',
                        href: 'https://www.bilibili.com',
                        blankTarget: true
                    },
                    {
                        key: 'github',
                        icon: 'logo-github',
                        href: 'https://baidu.com',
                        blankTarget: true
                    },
                    {
                        key: '条款',
                        title: '条款',
                        href: '',
                        blankTarget: true
                    }
                ],
                copyright: 'Copyright © whatever'
            }
        }
    }
</script>