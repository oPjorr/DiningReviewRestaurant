import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000', // URL da API Django
});

export default instance;
