<template>
  <div class="login-container">
    <div class="login-form">
      <h2>Faça login</h2>
      <form @submit.prevent="login">
        <div class="input-container">
          <input type="email" v-model="email" id="email" placeholder="Email" required />
        </div>
        <div class="input-container">
          <input type="password" v-model="password" id="password" placeholder="Senha" required />
        </div>
        <button type="submit">Entrar</button>
      </form>
      <p>Não tem uma conta? <a @click="toggleMode">Faça seu cadastro</a></p>
    </div>
  </div>
</template>

<script>
const apiUrl = 'http://localhost:5000';

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
      fetch(`${apiUrl}/login`, {
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
      .then(() => {
        // alert('Login realizado com sucesso!');
        // console.log('Token:', data.access_token);
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
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  /* background: linear-gradient(to bottom, black 50%, white 50%); */
}

.login-form {
  background-color: white;
  padding: 40px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 300px;
}

h2 {
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input-container {
  margin-bottom: 15px;
  width: 100%;
}

input {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

p {
  text-align: center;
  margin-top: 20px;
}

a {
  color: #4CAF50;
  cursor: pointer;
}
</style>
