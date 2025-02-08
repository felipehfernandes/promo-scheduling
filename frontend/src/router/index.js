import { createRouter, createWebHistory } from 'vue-router';
import ListPromotions from '../components/ListPromotions.vue';

const routes = [
  { path: '/promocoes', component: ListPromotions },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
