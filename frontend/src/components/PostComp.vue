<script>
import { RouterLink } from "vue-router";
export default {
  name: "PostComp",
  data() {
    return {};
  },
  components: {
    RouterLink,
  },
  props: {
    user_id: Number,
    id: Number,
    username: String,
    title: String,
    caption: String,
  },
};
</script>
<template>
  <div class="card md-6" style="width: 15rem">
    <!-- <h5 class="card-title">{{ username }}</h5> -->
    <RouterLink class="card-title" :to="`/account/${user_id}`">{{
      username
    }}</RouterLink>
    <img src="https://picsum.photos/200/300" class="card-img-top" alt="..." />
    <div class="card-body">
      <!-- <h5 class="card-title">{{ title }}</h5> -->
      <RouterLink active-class="card-title" :to="`/posts/${id}`">{{
        title
      }}</RouterLink>
      <p class="card-text">
        {{ caption }}
      </p>
    </div>
  </div>
</template>

<style></style>
