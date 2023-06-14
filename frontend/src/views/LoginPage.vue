<template>
  <div class="content-section">
    <body>
      <form @submit="onLogin">
        <!-- class named "container" is assigned to div -->
        <div class="container">
          <h1>Login Here</h1>

          <label for="email"><b>Email</b></label>
          <input
            type="text"
            placeholder="Enter Email"
            name="email"
            id="email"
            required
            v-model.trim="formData.email"
          />
          <div class="error" v-if="errors.email">{{ errors.email }}</div>

          <label for="pwd"><b>Password</b></label>
          <input
            type="password"
            placeholder="Enter Password"
            name="pwd"
            id="pwd"
            required
            v-model.trim="formData.password"
          />
          <div class="error" v-if="errors.password">{{ errors.password }}</div>
          <div class="error" v-if="error">{{ error }}</div>
          <button type="submit">Login</button>
        </div>

        <div>
          <p>Not a Member?<a href="/register">Sign Up</a>.</p>
        </div>
      </form>
    </body>
  </div>
</template>

<script>
import axios from "axios";
import SignupValidations from "@/services/SignupValidations";
export default {
  name: "LoginPage",
  data() {
    return {
      users: [],
      formData: {
        email: "",
        password: "",
      },
      errors: [],
      error: "",
    };
  },
  methods: {
    async onLogin(e) {
      e.preventDefault();
      let validations = new SignupValidations(
        this.formData.email,
        this.formData.password
      );
      this.errors = validations.checkValidations();
      if (Object.keys(this.errors).length) {
        return false;
      } else {
        let result = await axios.get(
          `http://127.0.0.1:5000/handle_get?email=${this.formData.email}&password=${this.formData.password}`
        );
        // let l = Object.keys(result.data).length;
        let l = JSON.stringify(result.data.status)
        // console.log(l);
        if (l === '"invalid credentials!"') {
          this.error = "invalid credentials!";
        } else if (l === '"404"') {
          alert("Error!!");
          this.error = "backend problem";
        } else {
          // this.initForm();
          // alert("Login Done!!");
          // console.log(JSON.stringify(result.data));
          localStorage.setItem("current-user", JSON.stringify(result.data));
          this.$router.push({ name: "HomePage" });
        }
      }
    },
  },
  mounted() {
    let user = localStorage.getItem("current-user");
    if (user) {
      this.$router.push({ name: "LoginPage" });
    }
  },
};
// getUsers() {
//   const path = "http://127.0.0.1:5000/users";

//   axios
//     .get(path)
//     .then((response) => {
//       // console.log(response.data.users);

//       this.users = response.data.users;
//       console.log(this.users);
//     })
//     .catch((error) => {
//       console.error(error);
//     });
// },
// initForm() {
//   (this.formData.email = ""), (this.formData.password = "");
// },
// userCheck(payload) {
//   this.getUsers();
// },
//     onSubmit(e) {
//       e.preventDefault();
//       let validations = new SignupValidations(
//         this.formData.email,
//         this.formData.password
//       );
//       this.errors = validations.checkValidations();
//       if (this.errors.length) {
//         return false;
//       }
//     },
//   },
//   created() {
//     this.getUsers();
//   },
// };
</script>
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  width: 25vw;
}
input {
  margin: 0.25em 0em 1em 0em;
  outline: none;
  padding: 0.5em;
  border: none;
  background-color: rgb(225, 225, 225);
  border-radius: 0.25em;
  color: black;
}
button {
  padding: 0.75em;
  border: none;
  outline: none;
  background-color: rgb(68, 18, 232);
  color: white;
  border-radius: 0.25em;
}

/* hover functionality for button */
button:hover {
  cursor: pointer;
  background-color: rgb(41, 4, 164);
}
</style>
