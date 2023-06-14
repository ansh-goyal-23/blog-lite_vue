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
            <h4>Are You Sure you want to delete this post?</h4>
            <form @submit.prevent="onDelete">
              <button type="submit" class="btn btn-danger">YES SURE</button>
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
        DELETE
      </button>
    </div>
  </div>
</template>

<script>
// import { useRoute } from "vue-router";
import axios from "axios";
export default {
  name: "DeletePost",
  data() {
    return {
      selectedFile: null,
      OpenClose: this.visible,
      post_id: "",
      result: "",
    };
  },
  props: {
    visible: Boolean,
    variant: String,
    id: String,
  },
  methods: {
    openCloseFun() {
      this.OpenClose = !this.OpenClose;
    },

    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },
    async onDelete() {
      this.result = await axios.delete(
        `http://127.0.0.1:5000/posts/${this.id}`
      );
      localStorage.setItem("current-post", JSON.stringify(this.result.data));
      console.log("Hello");
      this.$router.push({ name: "HomePage" });
    },
  },
  watch: {
    visible: function (newVal, oldVal) {
      this.OpenClose = newVal;
      console.warn(newVal, oldVal);
    },
  },

  mounted() {
    // const route = useRoute();
    // this.post_id = route.params.id;
    // console.log("Hello", this.post_id);
    // let post = localStorage.getItem("current-post");
    // if (post["id"] !== this.id) {
    // }
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
