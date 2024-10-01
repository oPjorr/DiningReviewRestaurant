<template>
    <div class="user-info">
      <div :class="{'superuser': isSuperUser}">
        {{ isSuperUser ? 'SuperUser - ' : '' }}{{ username }}
      </div>
    </div>
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
  import { useMainStore } from '../store/store';
  import { computed, onMounted } from 'vue';
  
  export default {
    setup() {
      const mainStore = useMainStore();
  
      onMounted(() => {
        mainStore.verifyToken();
        mainStore.fetchReviews();
      });
  
      const isAuthenticated = computed(() => mainStore.isAuthenticated);
      const reviews = computed(() => mainStore.reviews);
      const username = computed(() => mainStore.username);
      const isSuperUser = computed(() => mainStore.isSuperUser);
  
      return {
        isAuthenticated,
        reviews,
        username,
        isSuperUser,
      };
    },
  };
  </script>

<style>
.user-info {
    position: absolute;
    top: 10px;
    left: 10px;
    font-size: 16px;
  }
  .superuser {
    color: red;
  }
  
.reviews-container {
  max-width: 800px;
  margin: 2% auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 2em;
  margin-bottom: 20px;
  color: #333;
  text-align: center;
}

.reviews-list {
  list-style: none;
  padding: 0;
}

.review-item {
  padding: 15px;
  margin-bottom: 10px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
}

.review-user {
  font-weight: bold;
  color: #007BFF;
}

.review-comment {
  margin-left: 10px;
  color: #555;
}

.review-rating {
  margin-left: 10px;
  color: #FFD700;
}
</style>
