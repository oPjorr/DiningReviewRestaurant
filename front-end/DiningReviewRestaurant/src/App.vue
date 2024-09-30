<script setup>
import ReviewList from './components/ReviewList.vue'
import Register from './components/Register.vue'
import Login from './components/Login.vue'
</script>

<template>
  <div id="app">
    <nav>
      <router-link to="/login">Login</router-link>
      <router-link to="/register">Register</router-link>
      <router-link to="/reviews">Reviews</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: 'App',
};
</script>
<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
