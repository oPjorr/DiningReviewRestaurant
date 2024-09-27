<template>
  <div>
    <h1>Reviews</h1>
    <ul>
      <li v-for="review in reviews" :key="review.id">
        {{ review.user}}: {{ review.comment }} ({{ review.rating }} estrelas)
      </li>
    </ul>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      reviews: [],
    };
  },
  created() {
    this.fetchReviews();
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
