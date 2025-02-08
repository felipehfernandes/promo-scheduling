<template>
  <div class="register-container">
    <h2>Registrar</h2>
    <form @submit.prevent="register">
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" id="email" required>
      </div>
      <div>
        <label for="password">Senha:</label>
        <input type="password" v-model="password" id="password" required>
      </div>
      <button type="submit">Registrar</button>
    </form>
    <p>Já tem uma conta? <a @click="toggleMode">Faça login</a></p>
  </div>
</template>

<script>
export default {
  name: 'RegisterForm',
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    register() {
      fetch('http://localhost:5000/register', {
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
      .then(() => {
        alert('Registro realizado com sucesso!');
      })
      .catch(error => {
        console.error('Erro ao registrar:', error);
        alert('Erro ao registrar: ' + error.message);
      });
    },
    toggleMode() {
      this.$emit('toggle-mode');
    }
  }
};
</script>

<style scoped>
.register-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}
label {
  display: block;
  margin-bottom: 5px;
}
input {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  width: 100%;
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #45a049;
}
p {
  text-align: center;
}
a {
  cursor: pointer;
  color: #4CAF50;
}
</style>
