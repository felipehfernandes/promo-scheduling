<template>
  <div>
    <h2>Promoções</h2>
    <table>
      <thead>
        <tr>
          <th>Nome</th>
          <th>Valor</th>
          <th>Data Início</th>
          <th>Data Fim</th>
          <th>Status</th>
          <th>Regiões</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="promocao in promocoes" :key="promocao.id">
          <td>{{ promocao.nome_promocao }}</td>
          <td>{{ promocao.valor_promocao }}</td>
          <td>{{ promocao.data_inicio }}</td>
          <td>{{ promocao.data_fim }}</td>
          <td>{{ promocao.status }}</td>
          <td>{{ promocao.regioes.join(', ') }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      promocoes: []
    };
  },
  created() {
    fetch('http://localhost:5000/promocoes')
      .then(response => response.json())
      .then(data => {
        this.promocoes = data;
      })
      .catch(error => console.error('Erro ao carregar promoções:', error));
  },
  methods: {
    editarPromocao(id) {
      this.$router.push({ name: 'AddPromocao', params: { promoId: id } });
    }
  }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
}
th {
  background-color: #f2f2f2;
}
</style>
