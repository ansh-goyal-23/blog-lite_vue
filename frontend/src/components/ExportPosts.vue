<template>
  <div>
    <button
      type="button"
      class="btn btn-info action_btn"
      v-on:click="downloadCSVData"
    >
      Export Blogs
    </button>
  </div>
</template>

<script>
import { useRoute } from "vue-router";
import axios from "axios";
export default {
  name: "ExportPosts",
  data() {
    return {
      csvdata: [
      ],
      author: "",
      title: "",
      content: "",
      date_added: "",
    };
  },
  props: {
    user_id: Number,
  },
  methods: {
    onGet() {
      downloadCSVData();
    },
    async downloadCSVData() {
      let path = `http://127.0.0.1:5000/export_posts?user_id=${this.user_id}`;
      let result = await axios.get(path);
      if (result.data) {
        this.csvdata = result.data;
        let csv = "Author,Title,Content,Date_Added\n";
        this.csvdata.forEach((row) => {
          csv += row.join(",");
          csv += "\n";
        });

        const anchor = document.createElement("a");
        anchor.href = "data:text/csv;charset=utf-8," + encodeURIComponent(csv);
        anchor.target = "_blank";
        anchor.download = "blogslite.csv";
        anchor.click();
      } else {
        this.posts = [];
      }
      // let l = Object.keys(result.data).length
      // console.log("Feedcomp", result.data)
    },
  },
};
</script>

<style scoped>
.content-section {
  background: #ffffff;
  padding: 10px 20px;
  border: 1px solid #dddddd;
  border-radius: 3px;
  margin-bottom: 20px;
}
</style>
