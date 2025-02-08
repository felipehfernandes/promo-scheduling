<template>
  <div class="login-container" style="display: flex; justify-content: center; align-items: center; height: 100vh; background: linear-gradient(to bottom, black 50%, white 50%);">
    <div style="background-color: white; padding: 40px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); width: 300px;">
      <h2 style="text-align: center;">Faça login</h2>
      <form @submit.prevent="login" style="display: flex; flex-direction: column; align-items: center;">
        <div style="margin-bottom: 15px; width: 80%;">
          <input type="email" v-model="email" id="email" placeholder="Email" required style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <div style="margin-bottom: 15px; width: 80%;">
          <input type="password" v-model="password" id="password" placeholder="Senha" required style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <button type="submit" style="width: 80%; padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">Entrar</button>
      </form>
      <p style="text-align: center; margin-top: 20px;">Não tem uma conta? <a @click="toggleMode" style="color: #4CAF50; cursor: pointer;">Faça seu cadastro</a></p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    login() {
      fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: this.email, password: this.password })
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro ao logar.');
        }
        return response.json();
      })
      .then(data => {
        alert('Login realizado com sucesso!');
        console.log('Token:', data.access_token);
        this.$emit('authenticate');
      })
      .catch(error => {
        console.error('Erro ao logar:', error);
        alert('Erro ao logar.');
      });
    },
    toggleMode() {
      this.$emit('toggle-mode');
    }
  }
};
</script>

<style scoped>
/* Removed styles as they are now inline */
</style>
