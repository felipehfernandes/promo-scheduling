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
  console.log(`Navigating to: ${to.path}`);
  const isAuthenticated = !!localStorage.getItem('authToken');
  console.log(`User is authenticated: ${isAuthenticated}`);
  if (to.name !== 'Login' && !isAuthenticated) {
    next({ name: 'Login' });
  } else {
    next();
  }
});

export default router;
