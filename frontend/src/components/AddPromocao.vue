<template>
  <div>
    <h2>Criar Promoção</h2>
    <form @submit.prevent="adicionarPromocao()">
      <div>
        <label for="nome_promocao">Nome da Promoção:</label>
        <input type="text" v-model="novaPromocao.nome_promocao" id="nome_promocao" required />
      </div>
      <div>
        <label for="valor_promocao">Valor da Promoção:</label>
        <input type="number" v-model="novaPromocao.valor_promocao" id="valor_promocao" required />
      </div>
      <div>
        <label for="data_inicio">Data de Início:</label>
        <input type="datetime-local" v-model="novaPromocao.data_inicio" id="data_inicio" required />
      </div>
      <div>
        <label for="data_fim">Data de Fim:</label>
        <input type="datetime-local" v-model="novaPromocao.data_fim" id="data_fim" required />
      </div>
      <div>
        <label for="status">Status:</label>
        <select v-model="novaPromocao.status" id="status">
          <option :value="1">Vigente</option>
          <option :value="2">Desativado</option>
        </select>
      </div>
      <div>
        <label for="regioes">Regiões:</label>
        <multiselect v-model="selectedRegioes" :options="regioes" :multiple="true" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Selecione as regiões" label="nome" track-by="id"></multiselect>
      </div>
      <button type="submit">Criar Promoção</button>
    </form>
    <div v-if="errorMessage" class="error-box">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script>
import Multiselect from 'vue-multiselect';
import 'vue-multiselect/dist/vue-multiselect.min.css';

export default {
  components: { Multiselect },
  data() {
    return {
      novaPromocao: {
        nome_promocao: '',
        valor_promocao: '',
        data_inicio: '',
        data_fim: '',
        status: 1,
        regioes: []
      },
      regioes: [],
      selectedRegioes: [],
      errorMessage: ''
    };
  },
  created() {
    this.fetchRegioes();
  },
  methods: {
    fetchRegioes() {
      fetch('http://localhost:5000/regioes')
        .then(response => response.json())
        .then(data => {
          this.regioes = data.map(regiao => ({ id: regiao.id, nome: regiao.nome }));
        })
        .catch(error => {
          console.error('Erro ao carregar regiões:', error);
          this.errorMessage = 'Erro ao carregar regiões: ' + error.message;
        });
    },
    adicionarPromocao() {
      const promocao = {
        nome_promocao: this.novaPromocao.nome_promocao,
        valor_promocao: this.novaPromocao.valor_promocao,
        data_inicio: this.novaPromocao.data_inicio,
        data_fim: this.novaPromocao.data_fim,
        status: this.novaPromocao.status,
        regioes_ids: this.selectedRegioes.map(regiao => regiao.id).join(',')
      };
      fetch('http://localhost:5000/promocoes', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(promocao)
      })
      .then(response => {
        if (!response.ok) {
          return response.json().then(err => { throw new Error(err.error); });
        }
        return response.json();
      })
      .then(() => {
        alert('Promoção criada com sucesso!');
        this.novaPromocao = {
          nome_promocao: '',
          valor_promocao: '',
          data_inicio: '',
          data_fim: '',
          status: 1,
          regioes: []
        };
        this.selectedRegioes = [];
        this.errorMessage = '';
      })
      .catch(error => {
        console.error('Erro ao criar promoção:', error);
        this.errorMessage = 'Erro ao criar promoção: ' + error.message;
      });
    }
  }
};
</script>

<style scoped>
div {
  margin-bottom: 10px;
}
label {
  display: block;
}
input {
  margin-top: 5px;
  margin-bottom: 10px;
}
button {
  padding: 5px 10px;
}
.error-box {
  color: red;
  margin-top: 10px;
}
</style>
