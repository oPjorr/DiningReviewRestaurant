  import { defineStore } from 'pinia';
  import axios from 'axios';

  export const useMainStore = defineStore('main', {
    state: () => ({
      isAuthenticated: false,
      reviews: [],
      username: '',
      isSuperUser: false,
    }),
    actions: {
      async verifyToken() {
        const token = localStorage.getItem('token');
        if (token) {
          try {
            const response = await axios.post('https://diningreviewrestaurant-api.onrender.com/api/token/verify/', { token });
            this.isAuthenticated = true;
            console.log('Token verificado com sucesso');
            await this.fetchUserInfo();
          } catch (error) {
            this.isAuthenticated = false;
            console.error('Erro ao verificar token:', error);
          }
        } else {
          this.isAuthenticated = false;
          console.log('Token não encontrado');
        }
      },
      
      async fetchUserInfo() {
        try {
          const response = await axios.get('https://diningreviewrestaurant-api.onrender.com/api/user/', {
            headers: {
              Authorization: `Bearer ${localStorage.getItem('token')}`,
            },
          });
          this.username = response.data.username;
          this.isSuperUser = response.data.is_superuser;
          console.log('Informações do usuário carregadas:', response.data);
        } catch (error) {
          console.error('Erro ao buscar informações do usuário:', error);
        }
      },      
      async fetchReviews() {
        if (this.isAuthenticated) {
          try {
            const response = await axios.get('https://diningreviewrestaurant-api.onrender.com/reviews/', {
              headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
              },
            });
            this.reviews = response.data;
          } catch (error) {
            console.error('Failed to fetch reviews:', error);
          }
        }
      },
    },
  });
  