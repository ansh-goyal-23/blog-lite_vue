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
            <h5 class="modal-title">Modal title</h5>
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
            <h3>Add a Blog/Post</h3>
            <form @submit="onUpload">
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
                  accept=".png, .jpg, .jpeg"
                  :maxFileSize="1000000"
                  ref="fileInput"
                  @change="onFileSelected"
                />
              </div>
              <button type="submit" class="btn btn-primary">POST</button>
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
        Add Post
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "AddPost",
  data() {
    return {
      selectedFile: null,
      OpenClose: this.visible,
      title: "",
      content: "",
      file: null,
      url: "https://picsum.photos/200/300",
    };
  },
  props: {
    visible: Boolean,
    variant: String,
    user_id: Number,
  },
  methods: {
    openCloseFun() {
      this.OpenClose = !this.OpenClose;
    },

    onFileSelected(event) {
      // console.log(event)
      this.file = event.target.files[0];
      // console.log(this.file)
      // this.url = URL.createObjectURL(this.file)
      // console.log(this.url)
      // var imageFile = document.querySelector('#imageUpload')
    },
    async onUpload() {
      let path = "http://127.0.0.1:5000/upload_post";
      const payload = {
        user_id: this.user_id,
        title: this.title,
        content: this.content,
      };
      // payload.append
      // console.log(payload);
      let result = await axios.post(path, payload);
      // console.log(result);
      // .then((res) => {
      //   console.log("res");
      // });
    },
  },
  watch: {
    visible: function (newVal, oldVal) {
      this.OpenClose = newVal;
      console.log(newVal, oldVal);
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
