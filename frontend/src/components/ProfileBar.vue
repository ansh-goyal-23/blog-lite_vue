<template>
  <div class="content-section">
    <div class="media">
      <!-- <img class="rounded-circle account-img" src="&image_file"> -->
      <div class="media-body">
        <h2 class="account-heading">{{ username }}</h2>
        <p class="text-secondary">{{ email }}</p>
      </div>
    </div>

    <div class="container">
      <div class="row">
        <div class="col-md-3" for="post_count">{{ post_count }}</div>
        <div class="col-md-6" for="followers_count">{{ followers_count }}</div>
        <div class="col-md-3" for="following_count">{{ followings_count }}</div>
        <div class="col-md-3">Posts</div>
        <div class="col-md-6">Followers</div>
        <div class="col-md-3">Following</div>
      </div>
    </div>
  </div>
</template>

<script>
// import AddPost from "./AddPost.vue";
export default {
  name: "ProfileBar",
  props: {
    username: String,
    email: String,
    post_count: Number,
    followers_count: Number,
    followings_count: Number,
  },
  methods: {},
  components: {
    // AddPost,
  },
};
</script>

<style scoped></style>
