<template>
  <div class="register-container" style="display: flex; justify-content: center; align-items: center; height: 100vh; background: linear-gradient(to bottom, black 50%, white 50%);">
    <div style="background-color: white; padding: 40px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); width: 300px;">
      <h2 style="text-align: center;">Faça o cadastro</h2>
      <form @submit.prevent="register" style="display: flex; flex-direction: column; align-items: center;">
        <div style="margin-bottom: 15px; width: 100%;">
          <input type="email" v-model="email" id="email" placeholder="Email" required style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <div style="margin-bottom: 15px; width: 100%;">
          <input type="password" v-model="password" id="password" placeholder="Senha" required style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <div style="margin-bottom: 15px; width: 100%;">
          <input type="password" v-model="confirmPassword" id="confirmPassword" placeholder="Confirme a Senha" required style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <button type="submit" style="width: 100%; padding: 10px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">Registrar</button>
      </form>
      <p style="text-align: center; margin-top: 20px;">Já tem uma conta? <a @click="toggleMode" style="color: #4CAF50; cursor: pointer;">Faça login</a></p>
    </div>
  </div>
</template>

<script>
const apiUrl = 'http://localhost:5000';

export default {
  name: 'RegisterForm',
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: ''
    };
  },
  methods: {
    register() {
      if (this.password.length < 8) {
        alert('A senha deve ter mais de 8 caracteres.');
        return;
      }
      if (this.password !== this.confirmPassword) {
        alert('As senhas não são iguais.');
        return;
      }
      fetch(`${apiUrl}/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: this.email, password: this.password })
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro ao registrar.');
        }
        return response.json();
      })
      .then(() => {
        alert('Registro realizado com sucesso!');
        this.$emit('toggle-mode');
      })
      .catch(error => {
        console.error('Erro ao registrar:', error);
        alert('Erro ao registrar.');
      });
    },
    toggleMode() {
      this.$emit('toggle-mode');
    }
  }
};
</script>

<style scoped>
/* Removed styles as they are now inline in the template */
</style>
