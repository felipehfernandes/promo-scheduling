import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import { io } from 'socket.io-client';

// import Toast from 'vue-toastification';
// import 'vue-toastification/dist/index.css';

createApp(App)
  .use(router)  // Integrar o roteador
  .use(store)   // Integrar o Vuex store
  // .use(Toast) // Configure Vue Toastification
  .mount('#app');

const socket = io('http://localhost:5000');

socket.on('connect', () => {
  console.log('Connected to WebSocket server');
});

socket.on('notification', (message) => {
  // Display notification
  console.log('Notification received:', message);
});
