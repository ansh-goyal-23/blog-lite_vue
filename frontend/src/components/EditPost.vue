<template>
  <div>
    <!-- </div> -->
    <div
      v-if="OpenClose"
      class="modal fade show"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalLabel"
      aria-modal="true"
      style="display: block"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h6 class="modal-title">UPDATE BLOG</h6>
            <button
              type="button"
              class="close"
              @click="openCloseFun"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <h3>Update the Blog/Post</h3>
            <form @submit="onUpdate">
              <div class="row mb-3">
                <label for="title" class="col-sm-2 col-form-label">Title</label>
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control"
                    id="title"
                    v-model="title"
                  />
                </div>
              </div>
              <div class="row mb-3">
                <label for="caption" class="col-sm-2 col-form-label"
                  >Caption</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control"
                    id="caption"
                    v-model="content"
                  />
                </div>
              </div>
              <div class="mb-3">
                <label for="imageFile" class="form-label">Image</label>
                <input
                  class="form-control"
                  type="file"
                  id="imageFile"
                  @change="onFileSelected"
                />
              </div>
              <button type="submit" class="btn btn-primary">UPDATE</button>
            </form>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              @click="openCloseFun"
              :class="'btn btn-' + variant"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal-footer">
      <button type="button" @click="openCloseFun" :class="'btn btn-' + variant">
        UPDATE
      </button>
    </div>
  </div>
</template>

<script>
import { useRoute } from "vue-router";
import axios from "axios";
export default {
  name: "EditPost",
  data() {
    return {
      selectedFile: null,
      OpenClose: this.visible,
      title: "",
      content: "",
      post_id: "",
    };
  },
  props: {
    visible: Boolean,
    variant: String,
    username: String,
  },
  methods: {
    openCloseFun() {
      this.OpenClose = !this.OpenClose;
    },

    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },
    async onUpdate() {
      let path = `http://127.0.0.1:5000/posts/${this.post_id.id}`;
      console.log(path);
      const payload = {
        id: this.post_id.id,
        author: this.username,
        title: this.title,
        content: this.content,
      };
      console.log("hello", payload);
      let result = await axios.post(path, payload);
      console.log(result);
    },
  },
  watch: {
    visible: function (newVal, oldVal) {
      this.OpenClose = newVal;
      console.log(newVal, oldVal);
    },
  },
  async mounted() {
    const route = useRoute();
    this.post_id = route.params;
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
