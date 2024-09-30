<template>
  <div class="reviews-container" v-if="isAuthenticated">
    <h1 class="title">Reviews</h1>
    <ul class="reviews-list">
      <li v-for="review in reviews" :key="review.id" class="review-item">
        <span class="review-user">{{ review.reviewer_name }}</span>: 
        <span class="review-comment">{{ review.comment }}</span> 
        <span class="review-rating"> ({{ review.rating }} estrelas)</span>
      </li>
    </ul>
  </div>
  <div v-else><p>Por favor, faça login para ver o conteúdo exclusivo.</p></div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      reviews: [],
      isAuthenticated: false,
    };
  },
  created() {
    this.fetchReviews();
    const token = localStorage.getItem('token');
    console.log(this.isAuthenticated)
    console.log(token);
        if (token) {
            this.isAuthenticated = true;
            console.log(this.isAuthenticated);
        }
  },
  methods: {
    async fetchReviews() {
      try {
        const response = await axios.get('reviews/');
        this.reviews = response.data;
      } catch (error) {
        console.error('Erro ao buscar reviews:', error);
      }
    },
  },
};
</script>

<style scoped>
.reviews-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-top: 5%;
}

.title {
  font-size: 2em;
  color: #333;
  text-align: center;
  margin-bottom: 20px;
}

.reviews-list {
  list-style-type: none;
  padding: 0;
}

.review-item {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px;
  margin-bottom: 10px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.review-user {
  font-weight: bold;
  color: #555;
}

.review-comment {
  color: #666;
}

.review-rating {
  color: #f39c12;
}
</style>
