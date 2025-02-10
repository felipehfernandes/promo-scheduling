<template>
  <div class="main-content">
    <h2>Promoções</h2>
    <table class="promocoes-table">
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
        <tr v-for="(promocao, index) in promocoes" :key="promocao.id" :style="getRowStyle(index)">
          <td>{{ promocao.nome_promocao }}</td>
          <td>{{ formatCurrency(promocao.valor_promocao) }}</td>
          <td>{{ formatDate(promocao.data_inicio) }}</td>
          <td>{{ formatDate(promocao.data_fim) }}</td>
          <td>{{ promocao.status === 'vigente' ? 'Vigente' : 'Desativado' }}</td>
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
    },
    formatDate(date) {
      const d = new Date(date);
      const day = String(d.getDate()).padStart(2, '0');
      const month = String(d.getMonth() + 1).padStart(2, '0');
      const year = d.getFullYear();
      const hours = String(d.getHours()).padStart(2, '0');
      const minutes = String(d.getMinutes()).padStart(2, '0');
      return `${day}/${month}/${year} ${hours}:${minutes}`;
    },
    formatCurrency(value) {
      return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
      }).format(value);
    },
    getRowStyle(index) {
      return {
        backgroundColor: index % 2 === 0 ? 'rgb(249 250 251)' : 'white'
      };
    }
  }
};
</script>

<style scoped>
.main-content {
  padding: 1.5rem;
  background-color: rgb(249 250 251);
  display: flex;
  flex-direction: column;
  align-items: center;
}

h2 {
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
}

.promocoes-table {
  width: 100%;
  max-width: 1200px;
  border-collapse: collapse;
  margin: 20px 0;
}

th, td {
  padding: 10px;
  text-align: left;
  font-size: 0.875rem;
}

th {
  background-color: #f2f2f2;
  text-transform: uppercase;
  font-weight: bold;
}

td {
  word-wrap: break-word;
}

tr:nth-child(even) {
  background-color: rgb(249 250 251);
}

tr:nth-child(odd) {
  background-color: white;
}
</style>
