<style>

#pdf-content {
	width: 100%;
	height: 100%;
	top: 0;
	left: 0%;
}

</style>


<template>
    <Alert v-if="showSuccess" type="success" closable @on-close="this.showSuccess=false">
        <p style="text-align: center;">Submit Succeeded</p>
    </Alert>
    <Alert v-if="showError" type="error" closable @on-close="this.showError=false">
        <p style="text-align: center;">Unauthorized! Please Log In First.</p>
    </Alert>
    <div style="display: flex;">
        <div style="flex: 1; height: 90vh; padding: 0; margin: 0;">
            <div id="pdf-content" style="padding: 0; margin: 0;" />
        </div>
        <div style="flex: 1;">
            <div style="display: flex;">
                <Input v-model="title" prefix="ios-bookmarks" placeholder="Enter Title..." style="flex: 2;" />
                <Button @click="submit" icon="ios-cloud-upload-outline" type="success" long style="flex: 1;">SUBMIT</Button>
            </div>
            <v-md-editor v-model="text" height="86vh"></v-md-editor>
        </div>
    </div>
</template>

<script>

import axios from 'axios';
import pdf from 'pdfobject'


export default {
    data() {
        return {
            paper_id: String,
            pdfTop: 40,
            showTips: true,
            text: '',
            title: '',
            showSuccess: false,
            showError: false
        };
    },
    methods: {
        init() {
            this.title = this.$store.state.pdf.title;
            this.text = this.$store.state.pdf.text;
            this.paper_id = this.$store.state.pdf.pdf_id;
            const paper_url = "http://localhost:82/static/" + this.paper_id + ".pdf";
            this.$nextTick(function() {
                pdf.embed(paper_url, '#pdf-content')
            })
        },
        async submit() {
            await axios.post('/notes', {
                'title': this.title,
                'content': this.text,
                'pdf_id': this.paper_id
            })
                .then(response => {
                    if (response.status == 200) {
                        console.log('succeeded');
                        this.showSuccess = true;
                    }
                })
                .catch(error => {
                    console.log(error);
                    this.showError = true;
                })
        }
    },
    mounted() {
        this.init();
    }
};
</script>