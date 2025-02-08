<template>
  <div class="login-container" style="display: flex; justify-content: center; align-items: center; height: 100vh;">
    <div style="background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
      <h2 style="text-align: center;">Informe seu email</h2>
      <form @submit.prevent="login">
        <div style="margin-bottom: 15px;">
          <label for="email">Email:</label>
          <input type="email" v-model="email" id="email" required style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <div style="margin-bottom: 15px;">
          <label for="password">Senha:</label>
          <input type="password" v-model="password" id="password" required style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <button type="submit" style="width: 100%; padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;">Entrar</button>
      </form>
      <p style="text-align: center; margin-top: 20px;">Não tem uma conta? <a @click="toggleMode">Registre-se</a></p>
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
          return response.json().then(err => { throw new Error(err.error); });
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
        alert('Erro ao logar: ' + error.message);
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
