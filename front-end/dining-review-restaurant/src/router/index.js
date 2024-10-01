// router.js
import { createRouter, createWebHistory } from 'vue-router';
import { useMainStore } from '../store/store';
import Reviews from '../components/ReviewList.vue';
import Login from '../components/Login.vue';

const routes = [
  {
    path: '/reviews',
    component: Reviews,
    meta: { requiresAuth: true },
  },
  {
    path: '/login',
    component: Login,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const mainStore = useMainStore();
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!mainStore.isAuthenticated) {
      next({ path: '/login' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
