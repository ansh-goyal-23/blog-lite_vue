<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">Blog Lite</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarTogglerDemo02"
        aria-controls="navbarTogglerDemo02"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
        <!-- <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-item nav-link" to="/about"
              >About</router-link
            >
          </li>
        </ul> -->
        <form class="navbar-nav me-auto mb-6 mb-lg-0">
          <button v-on:click="logout" class="active">Logout</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  props: {
    msg: String,
  },
  methods: {
    logout() {
      console.log("Logout");
      localStorage.clear();
      this.$router.push({ name: "LoginPage" });
    },
  },
};
</script>

<style scoped></style>
