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
                        title: '别点',
                        href: 'https://www.bilibili.com',
                        blankTarget: true
                    },
                    {
                        key: 'github',
                        icon: 'logo-github',
                        href: 'https://github.com/BetulaSuk/DGD-B-6-WebsiteSource',
                        blankTarget: true
                    },
                    {
                        key: '条款',
                        title: '点我',
                        href: 'https://anime.bang-dream.com/mygo/',
                        blankTarget: true
                    }
                ],
                copyright: 'Copyright © Whatever'
            }
        }
    }
</script>