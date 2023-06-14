<template>
  <div class="content-section">
    <body>
      <form @submit="signUp">
        <!-- class named "container" is assigned to div -->
        <div class="container">
          <h1>Register Here</h1>
          <p>Kindly fill in this form to register.</p>
          <label for="username"><b>Username</b></label>
          <input
            type="text"
            placeholder="Enter username"
            name="username"
            id="username"
            required
            v-model.trim="formData.username"
          />

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

          <label for="password"><b>Password</b></label>
          <input
            type="password"
            placeholder="Enter Password"
            name="password"
            id="password"
            required
            v-model.trim="formData.password"
          />
          <div class="error" v-if="errors.password">{{ errors.password }}</div>

          <label for="confirm_password"><b>Repeat Password</b></label>
          <input
            type="password"
            placeholder="Confirm Password"
            name="confirm_password"
            id="confirm_password"
            required
            v-model.trim="formData.confirm_password"
          />
          <div class="error" v-if="errors.confirm_password">
            {{ errors.confirm_password }}
          </div>

          <button type="submit">Register</button>
        </div>

        <div>
          <p>Already have an account? <a href="/login">Log in</a>.</p>
        </div>
      </form>
    </body>
  </div>
</template>

<script>
import axios from "axios";
import SignupValidations from "@/services/SignupValidations";
export default {
  name: "RegisterPage",
  data() {
    return {
      users: [],
      formData: {
        username: "",
        email: "",
        password: "",
        confirm_password: "",
      },
      errors: [],
    };
  },
  methods: {
    async signUp(e) {
      e.preventDefault();
      console.warn("signUp");
      let validations = new SignupValidations(
        this.formData.email,
        this.formData.password
      );
      this.errors = validations.checkValidations();
      if (this.formData.password !== this.formData.confirm_password) {
        this.errors["confirm_password"] = "must be same as password";
      }
      console.log("Errors :", Object.keys(this.errors).length, this.errors);
      if (Object.keys(this.errors).length) {
        return false;
      } else {
        const payload = {
          username: this.formData.username,
          email: this.formData.email,
          password: this.formData.password,
        };
        console.log(payload);
        let result = await axios.post("http://127.0.0.1:5000/users", payload);
        console.log(result);
        if (result.status == 200) {
          // this.initForm();
          // alert("SignUp Done!!");
          console.log(JSON.stringify(result.data));
          // localStorage.setItem(
          //   "current-user",
          //   JSON.stringify(result.data.users)
          // );
          this.$router.push({ name: "LoginPage" });
        }
      }
    },

    // getUsers() {
    //   const path = "http://127.0.0.1:5000/users";

    //   axios
    //     .get(path)
    //     .then((response) => {
    //       console.log(response.data.users);
    //       this.users = response.data.users;
    //     })
    //     .catch((error) => {
    //       console.error(error);
    //     });
    // },
    // async addUser(payload) {
    //   const path = "http://127.0.0.1:5000/users";

    //   result = await axios
    //     .post(path, payload)
    //     .then(() => {
    //       this.getUsers();
    //     })
    //     .catch((error) => {
    //       console.error(error);
    //       this.getUsers();
    //     });
    // },
    initForm() {
      (this.formData.username = ""),
        (this.formData.email = ""),
        (this.formData.password = ""),
        (this.formData.confirm_password = "");
    },
    // onSubmit(e) {
    //   e.preventDefault();
    //   if (this.formData.confirm_password !== this.formData.password) {
    //     this.errors["confirm_password"] = "must be same as password";
    //     return false;
    //   } else {
    //     let validations = new SignupValidations(
    //       this.formData.email,
    //       this.formData.password
    //     );
    //     this.errors = validations.checkValidations();
    //     if (this.errors.length) {
    //       return false;
    //     } else {
    //       const payload = {
    //         username: this.formData.username,
    //         email: this.formData.email,
    //         password: this.formData.password,
    //       };
    //       console.log(payload);
    //       this.addUser(payload);
    //       // this.initForm();
    //     }
    //   }
    // },
    // onReset(e) {
    //   e.preventDefault();
    //   this.initForm();
    // },
  },
  created() {},
  async mounted() {
    let user = localStorage.getItem("current-user");
    if (user) {
      await this.$router.push({ name: "HomePage" });
    }
  },
};
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
