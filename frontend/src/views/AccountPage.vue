<template>
  <div>
    <ProfileBar
      :username="username"
      :email="email"
      :post_count="posts_count"
      :followers_count="followers_count"
      :followings_count="followings_count"
    ></ProfileBar>
    <ExportPosts :user_id="user_id"></ExportPosts>
    <PostPage></PostPage>
  </div>
</template>

<script>
import axios from "axios";
import { useRoute } from "vue-router";
import ProfileBar from "@/components/ProfileBar.vue";
// import PostsComp from "@/components/PostsComp.vue";
import ExportPosts from "@/components/ExportPosts.vue";
import PostPage from "./PostPage.vue";
export default {
  name: "AccontPage",
  data() {
    return {
      email: "",
      username: "",
      user_id: "",
      followers_count: null,
      followings_count: null,
      posts_count: null,
    };
  },
  components: {
    ProfileBar,
    ExportPosts,
    // PostsComp,
    PostPage,
  },
  async mounted() {
    const route = useRoute();
    this.user_id = route.params.id;
    // console.log(this.user_id);
    let path = `http://127.0.0.1:5000/user/${this.user_id}`;
    let path2 = `http://127.0.0.1:5000/counts/${this.user_id}`;
    // console.log(path);
    let result = await axios.get(path);
    let result2 = await axios.get(path2);
    this.followers_count = result2.data.followers_count
    this.posts_count = result2.data.posts_count
    this.followings_count = result2.data.followings_count
    
    // console.log(result2);
    this.username = result.data.username;
    this.email = result.data.email;
    this.user_id = result.data.user_id;
    // console.log(this.email);
    // let user = localStorage.getItem("current-user");
    // if (!user) {
    //   this.$router.push({ name: "RegisterPage" });
    // }
    // this.username = JSON.parse(user).username;
    // this.user_id = JSON.parse(user).user_id;
    // this.email = JSON.parse(user).email;
  },
};
</script>

<style scoped></style>
