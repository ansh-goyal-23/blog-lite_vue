<template>
  <div>
    <div v-for="post in posts" :key="post.id">
      <div v-if="posts.status != 'No Posts Found'" class="container">
        <div class="card" style="width: 15rem">
          <h5 class="flex-sm-fill text-sm-center">{{ post.author }}</h5>
          <!-- <h5>{{ post.post_img }}</h5> -->
          <img
            :src= imag
            class="card-img-top"
            alt="..."
          />
          <div class="card-body">
            <!-- <h5 class="card-title">{{ title }}</h5> -->
            
            
            <div v-if="post.user_id == owner_id" ><RouterLink active-class="card-title" :to="`/posts/${post.id}`">{{
              post.title
            }}</RouterLink></div>
            <h5 v-else class="card-title">{{ post.title }}</h5>
            <p class="card-text">
              {{ post.content }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { RouterLink } from "vue-router";
// import EditPost from "@/components/EditPost.vue";
// import DeletePost from "@/components/DeletePost.vue";
import { useRoute } from "vue-router";
import axios from "axios";
export default {
  name: "PostPage",
  data() {
    return {
      posts: [],
      imag: "https://picsum.photos/200/300",
      post: {
        username: "",
        content: "",
        title: "",
        author: "",
        post_img: ""
      },
      user_id: "",
      owner_id: "",
    };
  },
  components: {
    RouterLink,
    // EditPost,
    // DeletePost,
  },
  
  async mounted() {
    const route = useRoute();
    let user = localStorage.getItem("current-user");
    this.owner_id = JSON.parse(user).user_id;
    this.user_id = route.params.id;
    let path = `http://127.0.0.1:5000/get_posts?user_id=${this.user_id}`;
    // console.log(path);
    let result = await axios.get(path);
    if (result.data) {
      this.posts = result.data;
      console.log(result.data)
    } else {
      this.posts = [];
    }

    // console.log("postpage", this.posts.status);
    // this.post.username = result.data.author;
    // this.post.content = result.data.content;
    // this.post.title = result.data.title;
  },
};
</script>
<style scoped>
.container {
  margin-right: 1%;
  margin-left: 40%;
  margin-bottom: 20%;
  margin-top: 5%;
}
</style>
