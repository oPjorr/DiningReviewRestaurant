import { createRouter, createWebHistory } from 'vue-router';
import ReviewList from './components/ReviewList.vue';

const routes = [
  {
    path: '/',
    name: 'ReviewList',
    component: ReviewList,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
