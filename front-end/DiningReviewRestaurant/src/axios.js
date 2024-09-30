import axios from 'axios';

const instance = axios.create({
  baseURL: 'https://diningreviewrestaurant-api.onrender.com/', // URL da sua API Django
});

export default instance;
