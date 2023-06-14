<template>
  <div>
    <div>
      <nav class="nav nav-pills flex-column flex-sm-row">
        <RouterLink class="flex-sm-fill" :to="`/account/${user_id}`"
          >Welcome {{ name }}</RouterLink
        >
        <SearchBar
          class="flex-sm-fill text-sm-left"
          :visible="false"
          variant="success"
        >
        </SearchBar>
        <AddPost
          class="flex-sm-fill text-sm-center"
          :visible="false"
          variant="success"
          :user_id="user_id"
        ></AddPost>
      </nav>
    </div>
  </div>
</template>

<script>
import AddPost from "./AddPost.vue";
import SearchBar from "./SearchBar.vue";
export default {
  name: "WelcomeBar",
  data() {
    return {};
  },
  props: {
    name: String,
    user_id: Number,
  },
  components: {
    AddPost,
    SearchBar,
  },
};
</script>

<style scoped></style>
