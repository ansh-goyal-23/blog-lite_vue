import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import MainPage from "../views/MainPage.vue";
import RegisterPage from "../views/RegisterPage.vue";
import LoginPage from "../views/LoginPage.vue";
import AccountPage from "../views/AccountPage.vue";
// import PostPage from "../views/PostPage.vue";
import PostManagement from "../views/PostManagement.vue";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/main",
    name: "MainPage",
    component: MainPage,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/register",
    name: "RegisterPage",
    component: RegisterPage,
  },
  {
    path: "/account/:id",
    name: "AccountPage",
    component: AccountPage,
  },
  {
    path: "/posts/:id",
    name: "PostManagement",
    component: PostManagement,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
