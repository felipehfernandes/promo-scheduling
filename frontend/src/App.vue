<template>
  <div id="app">
    <SidebarMenu v-if="isAuthenticated" @navigate="navigate" />
    <component :is="currentComponent" @toggle-mode="toggleMode" @authenticate="authenticate" />
    <router-view></router-view> <!-- Adicionado para renderizar as rotas -->
  </div>
</template>

<script>
import LoginForm from './components/Login.vue';
import RegisterForm from './components/Register.vue';
import AddPromocao from './components/AddPromocao.vue';
import ListPromotions from './components/ListPromotions.vue';
import SidebarMenu from './components/Sidebar.vue';

export default {
  name: 'App',
  data() {
    return {
      currentComponent: 'LoginForm',
      isAuthenticated: false
    };
  },
  methods: {
    toggleMode() {
      this.currentComponent = this.currentComponent === 'LoginForm' ? 'RegisterForm' : 'LoginForm';
    },
    navigate(component) {
      console.log('Navigating to component:', component);
      this.currentComponent = component === 'CreatePromotion' ? 'AddPromocao' : 'ListPromotions';
      console.log('Current component set to:', this.currentComponent);
    },
    authenticate() {
      this.isAuthenticated = true;
      this.currentComponent = 'AddPromocao';
    }
  },
  components: {
    LoginForm,
    RegisterForm,
    AddPromocao,
    ListPromotions,
    SidebarMenu
  }
};
</script>

<style>
@import '@fontsource/inter';

#app {
  font-family: 'Inter', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
