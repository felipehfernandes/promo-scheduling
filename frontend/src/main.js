import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { io } from 'socket.io-client';

createApp(App)
  .use(router)  // Integrar o roteador
  .mount('#app');

const socket = io('http://localhost:5000');

socket.on('connect', () => {
  console.log('Connected to WebSocket server');
});

socket.on('notification', (message) => {
  // Display notification
  console.log('Notification received:', message);
});
