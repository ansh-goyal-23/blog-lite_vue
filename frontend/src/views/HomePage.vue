<template>
  <div>
    <WelcomeBar :name="name" :user_id="user_id" />
    <!-- <AddPost :visible="false" variant="success"></AddPost> -->
    <FeedComp></FeedComp>
  </div>
</template>

<script>
// import AddPost from "@/components/AddPost.vue";
import WelcomeBar from "@/components/WelcomeBar.vue";
import FeedComp from "@/components/FeedComp.vue";
export default {
  name: "HomePage",
  data() {
    return {
      name: "",
      user_id: null,
      activeModel: "",
    };
  },
  components: {
    // AddPost,
    WelcomeBar,
    FeedComp,
  },
  // inject: ["activeModel"],
  mounted() {
    let user = localStorage.getItem("current-user");

    if (!user) {
      this.$router.push({ name: "RegisterPage" });
    }
    this.name = JSON.parse(user).username;
    this.user_id = JSON.parse(user).user_id;
  },
};
</script>

<style scoped></style>
