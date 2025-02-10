<template>
  <div>
    <h1>Promoções</h1>
    <ul>
      <li v-for="promocao in promocoes" :key="promocao.id">
        {{ promocao.nome }} - {{ promocao.descricao }}
      </li>
    </ul>
  </div>
</template>

<script>
const apiUrl = 'http://localhost:5000';

export default {
  data() {
    return {
      promocoes: []
    };
  },
  created() {
    fetch(`${apiUrl}/promocoes`)
      .then(response => response.json())
      .then(data => {
        this.promocoes = data;
      })
      .catch(error => console.error('Erro ao carregar promoções:', error));
  }
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  padding: 5px 0;
}
</style>
