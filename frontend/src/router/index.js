import { createRouter, createWebHistory } from 'vue-router';
import ListPromotions from '../components/ListPromotions.vue';
import EditPromocao from '../components/EditPromocao.vue';

const routes = [
  { path: '/promocoes', component: ListPromotions },
  { path: '/promocoes/:id/editar', component: EditPromocao }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
