<template>
    <Button @click="value = true" type="primary">View information</Button>
        <Drawer :closable="false" width="640" v-model="value">
        <p class="words">Some information</p>
        </Drawer>
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