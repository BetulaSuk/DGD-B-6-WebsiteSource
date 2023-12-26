<style>

.title {
  text-align: center;
  font-size: 20px;
  font-weight: bold;
}

/*
.notes {
  width: 80vw;
  display: flex;
  flex-wrap: wrap;
}
*/



</style>

<template>
  <div>
    <section>
      <p class="title">My Notes</p>

      <div style="display: flex;">
        <div style="flex: 1;"></div>
        <div ref="scroll" v-scroll="handleScroll" style="height: 70vh; overflow: auto; flex: 4;">
          <div v-if="notes && notes.length" class="notes">
            <div v-for="(note, index) in notes" :key="note">
              <div class="card">
                <div class="card-body">
                    <p><strong>Note Title:</strong> {{ note.title }}</p>
                    <div><strong>Content:</strong> {{ note.content }}</div>
                    <Button type="primary" @click="viewPdf(notes[index])">View</Button>
                </div>
              </div>
              <br/>
            </div>
          </div>
          <div v-else>
            <p class="title">Nothing to see. Check back later.</p>
          </div>
        </div>
        <div style="flex: 1;"></div>
      </div>
    </section>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'DashboardView',
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getNotes');
  },
  computed: {
    ...mapGetters({ notes: 'stateNotes'}),
  },
  methods: {
    ...mapActions(['idSet', 'titleSet', 'textSet']),
    handleScroll(event) {
      const container = this.$refs.scroll;
      const deltaY = event.deltaY;
      container.scrollTop += deltaY;
    },
    async viewPdf(note) {
      await this.idSet(note.pdf.paper_id);
      await this.titleSet(note.title);
      await this.textSet(note.content);
      this.$router.push('/pdf');
    }
  },
});
</script>