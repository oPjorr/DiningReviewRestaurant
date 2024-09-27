<template>
    <div class="auth-container">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div>
          <label for="username">Username:</label>
          <input type="text" v-model="username" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" v-model="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('/login/', {
            username: this.username,
            password: this.password,
          });
          if (response.status === 200) {
            this.$router.push('/');
          }
        } catch (error) {
          console.error('Erro ao fazer login:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .auth-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .auth-container h2 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .auth-container form div {
    margin-bottom: 15px;
  }
  
  .auth-container label {
    display: block;
    margin-bottom: 5px;
  }
  
  .auth-container input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  
  .auth-container button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .auth-container button:hover {
    background-color: #0056b3;
  }
  </style>  