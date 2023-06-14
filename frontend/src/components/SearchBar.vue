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
            <h5 class="modal-title">Search Users</h5>
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
            <div class="container">
              <div
                class="row height d-flex justify-content-center align-items-center"
              >
                <div class="row-md-8">
                  <div class="search">
                    <i class="fa fa-search"></i>

                    <input
                      v-model="input_text"
                      type="text"
                      class="form-control"
                      placeholder="Enter Username"
                      v-on:change="Userlist"
                    />
                    <br />
                    <div class="container">
                      <div class="row" v-for="item in users" :key="item">
                        <div class="col-md-5" for="post_count">
                          {{ item[0] }}
                        </div>
                        <div class="col-md-3"></div>

                        <button
                          v-if="item[1] == 'UNFOLLOW'"
                          type="button"
                          class="col-md-4 flex-sm-fill text-sm-center"
                          @click="unFollowUser(item[0])"
                        >
                          {{ item[1] }}
                        </button>

                        <button
                          v-if="item[1] == 'FOLLOW'"
                          type="button"
                          class="col-md-4 flex-sm-fill text-sm-center"
                          @click="followUser(item[0])"
                        >
                          {{ item[1] }}
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
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
        Search
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SearchBar",
  data() {
    return {
      users: [],
      input_text: "",
      user_id: "",
      selectedFile: null,
      OpenClose: this.visible,
    };
  },
  props: {
    visible: Boolean,
    variant: String,
  },
  methods: {
    
    async Userlist() {
      let user = localStorage.getItem("current-user");
      this.user_id = JSON.parse(user).user_id;
      // console.log(this.user_id);
      let path = `http://127.0.0.1:5000/${this.user_id}/search/${this.input_text}`;

      let result = await axios.get(path);

      this.users = result.data;

      // console.log(this.users);
    },
    async followUser(username) {
      // console.log(username);
      let user = localStorage.getItem("current-user");
      this.user_id = JSON.parse(user).user_id;
      // console.log(this.user_id);

      let path = `http://127.0.0.1:5000/${this.user_id}/follow/${username}`;
      let result = await axios.get(path);

      console.log(result.data);
      this.Userlist();
      window.location.reload();

      // this.OpenClose = !this.OpenClose;
    },

    async unFollowUser(username) {
      let user = localStorage.getItem("current-user");
      this.user_id = JSON.parse(user).user_id;
      // console.log(this.user_id);
      // console.log(username);
      let path = `http://127.0.0.1:5000/${this.user_id}/unfollow/${username}`;
      // console.log(path);
      let result = await axios.get(path);

      console.log(result.data);
      this.Userlist();
      window.location.reload();
      // this.OpenClose = !this.OpenClose;
    },
    openCloseFun() {
      this.OpenClose = !this.OpenClose;
    },

    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },
  },
  watch: {
    visible: function (newVal, oldVal) {
      this.OpenClose = newVal;
      console.log(newVal, oldVal);
    },
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
  margin-left: 5px;
}
</style>
