<template>
  <div>
    <h2>Editar Promoção</h2>
    <form @submit.prevent="editarPromocao">
      <div>
        <label for="nome_promocao">Nome da Promoção:</label>
        <input type="text" v-model="promocao.nome_promocao" id="nome_promocao" required />
      </div>
      <div>
        <label for="valor_promocao">Valor da Promoção:</label>
        <input type="number" v-model="promocao.valor_promocao" id="valor_promocao" required />
      </div>
      <div>
        <label for="data_inicio">Data de Início:</label>
        <input type="datetime-local" v-model="promocao.data_inicio" id="data_inicio" required />
      </div>
      <div>
        <label for="data_fim">Data de Fim:</label>
        <input type="datetime-local" v-model="promocao.data_fim" id="data_fim" required />
      </div>
      <div>
        <label for="status">Status:</label>
        <select v-model="promocao.status" id="status">
          <option :value="1">Vigente</option>
          <option :value="2">Desativado</option>
        </select>
      </div>
      <div>
        <label for="regioes">Regiões:</label>
        <multiselect v-model="selectedRegioes" :options="regioes" :multiple="true" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Selecione as regiões" label="nome" track-by="id"></multiselect>
      </div>
      <button type="submit">Salvar Alterações</button>
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
      promocao: {
        nome_promocao: '',
        valor_promocao: '',
        data_inicio: '',
        data_fim: '',
        status: 1
      },
      selectedRegioes: [],
      regioes: [],
      errorMessage: ''
    };
  },
  created() {
    this.fetchRegioes();
    this.loadPromocao();
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
    loadPromocao() {
      const promocaoId = this.$route.params.id;
      fetch(`http://localhost:5000/promocoes/${promocaoId}`)
        .then(response => response.json())
        .then(data => {
          this.promocao = data;
          this.selectedRegioes = this.regioes.filter(regiao => data.regioes.includes(regiao.nome));
        })
        .catch(error => {
          console.error('Erro ao carregar promoção:', error);
          this.errorMessage = 'Erro ao carregar promoção: ' + error.message;
        });
    },
    editarPromocao() {
      const promocaoId = this.$route.params.id;
      const promocao = {
        nome_promocao: this.promocao.nome_promocao,
        valor_promocao: this.promocao.valor_promocao,
        data_inicio: this.promocao.data_inicio,
        data_fim: this.promocao.data_fim,
        status: this.promocao.status,
        regioes_ids: this.selectedRegioes.map(regiao => regiao.id).join(',')
      };
      fetch(`http://localhost:5000/promocoes/${promocaoId}`, {
        method: 'PUT',
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
        alert('Promoção atualizada com sucesso!');
        this.$router.push('/promocoes');
      })
      .catch(error => {
        console.error('Erro ao atualizar promoção:', error);
        this.errorMessage = 'Erro ao atualizar promoção: ' + error.message;
      });
    }
  }
};
</script>

<style scoped>
.error-box {
  color: red;
  margin-top: 10px;
}
</style>
