import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/', // URL da sua API Django
});

export default instance;
