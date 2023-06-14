<template>
  <div>
    <div class="container">
      <div class="card" style="width: 15rem">
        <h5 class="card-title">{{ post.author }}</h5>
        <img
          src="https://picsum.photos/200/300"
          class="card-img-top"
          alt="..."
        />
        <div class="card-body">
          <!-- <h5 class="card-title">{{ title }}</h5> -->
          <h5 class="card-title">{{ post.title }}</h5>
          <p class="card-text">
            {{ post.content }}
          </p>
        </div>
      </div>
    </div>
    <div class="row" v-if="user == post.user_id">
      <div class="col-2 col-sm-4">
        <EditPost
          class="flex-sm-fill text-sm-center"
          :visible="false"
          variant="success"
          :username="post.username"
        ></EditPost>
      </div>
      <div class="col-6 col-sm-4">
        <DeletePost
          class="flex-sm-fill text-sm-center"
          :visible="false"
          variant="success"
          :id="post_id"
        ></DeletePost>
      </div>
    </div>
  </div>
</template>

<script>
import EditPost from "@/components/EditPost.vue";
import DeletePost from "@/components/DeletePost.vue";
import { useRoute } from "vue-router";
import axios from "axios";
export default {
  name: "PostMangement",
  data() {
    return {
      user: "",
      posts: [],
      post: {
        content: "",
        title: "",
        author: "",
        user_id: "",
      },
      post_id: "",
    };
  },
  components: {
    EditPost,
    DeletePost,
  },
  async mounted() {
    const route = useRoute();
    this.post_id = route.params.id;
    let path = `http://127.0.0.1:5000/posts/${this.post_id}`;

    // console.log(path);
    let result = await axios.get(path);
    localStorage.setItem("current-post", JSON.stringify(result.data));
    this.user = JSON.parse(localStorage.getItem("current-user")).user_id
    console.log(this.user, result.data.user_id)

    // this.posts = result.data;
    // console.log("hello", this.posts);
    this.post.author = result.data.author;
    this.post.content = result.data.content;
    this.post.title = result.data.title;
    this.post.user_id = result.data.user_id;
  },
};
</script>

<style scoped>
.container {
  margin-right: 1%;
  margin-left: 35%;
  margin-bottom: 5%;
  margin-top: 2%;
}

.container2 {
  margin-right: 45%;
  margin-left: 30%;
  margin-bottom: 10%;
  margin-top: 1%;
}
</style>
