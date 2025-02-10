import { createRouter, createWebHistory } from 'vue-router';
import ListPromotions from '../components/ListPromotions.vue';
import Login from '../components/Login.vue';

const routes = [
  { path: '/promocoes', component: ListPromotions },
  { path: '/login', name: 'Login', component: Login },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('authToken');
  if (to.name !== 'Login' && !isAuthenticated) {
    next({ name: 'Login' });
  } else {
    next();
  }
});

export default router;
