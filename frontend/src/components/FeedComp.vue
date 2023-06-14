<template>
  <div class="container">
    <div class="cols row-cols-6" v-for="post in posts" :key="post.id">
      <PostComp
        :user_id="post.user_id"
        :id="post.id"
        :username="post.author"
        :caption="post.content"
        :title="post.title"
      ></PostComp>
      <br />
    </div>
  </div>
</template>

<script>
import PostComp from "./PostComp.vue";
import axios from "axios";
export default {
  name: "FeedComp",
  data() {
    return {
      posts: [],
      userid: "",
    };
  },
  components: {
    PostComp,
  },
  prop: {
    user_id: {
      type: String,
      required: false,
      default: "None",
    },
  },
  async mounted() {
    let user = localStorage.getItem("current-user");
    this.userid = JSON.parse(user).user_id;
    let result = await axios.get(
      // `http://127.0.0.1:5000/get_posts?user_id=${JSON.parse(user).user_id}`
      `http://127.0.0.1:5000/feed/${this.userid}`
    );
    // let l = Object.keys(result.data).length;
    if (result.data.status === "No Posts Found") {
      this.posts = [];
    } else {
      // console.log("Feedcomp", result.data)
      this.posts = result.data;
    }
    // console.log("Hello", this.posts);
  },
};
</script>

<style scoped>
.container {
  margin-right: 1%;
  margin-left: 40%;
  margin-bottom: 20%;
}
</style>
