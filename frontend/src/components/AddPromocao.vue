<template>
  <div class="main-content">
    <h2>Criar Promoção</h2>
    <form @submit.prevent="adicionarPromocao" class="form-container">
      <!-- Input para Nome da Promoção -->
      <div class="form-group">
        <label class="label">Nome da Promoção</label>
        <input
          type="text"
          v-model="novaPromocao.nome_promocao"
          placeholder="Nome da Promoção"
          required
        />
      </div>
      <!-- Input para Valor da Promoção -->
      <div class="form-group">
        <label class="label">Valor da Promoção</label>
        <input
          type="number"
          v-model="novaPromocao.valor_promocao"
          placeholder="Valor da Promoção"
          required
        />
      </div>
      <!-- Input para Data de Início -->
      <div class="form-group">
        <label class="label">Data de Início</label>
        <input
          type="datetime-local"
          v-model="novaPromocao.data_inicio"
          placeholder="Data de Início"
          required
        />
      </div>
      <!-- Input para Data de Fim -->
      <div class="form-group">
        <label class="label">Data de Fim</label>
        <input
          type="datetime-local"
          v-model="novaPromocao.data_fim"
          placeholder="Data de Fim"
          required
        />
      </div>
      <!-- Dropdown para Status -->
      <div class="form-group full-width">
        <label class="label">Status</label>
        <select v-model="novaPromocao.status" required>
          <option disabled value="">Selecione o status</option>
          <option :value="1">Vigente</option>
          <option :value="2">Desativado</option>
        </select>
      </div>
      <!-- Checkbox para Regiões -->
      <div class="form-group full-width">
        <label class="label">Regiões</label>
        <div style="display: flex; flex-wrap: wrap;">
          <div v-for="regiao in regioes" :key="regiao.id" class="checkbox-item">
            <input
              type="checkbox"
              :id="'checkbox-' + regiao.id"
              :value="regiao.id"
              v-model="novaPromocao.regioes"
              :name="'regiao-' + regiao.id"
            />
            <label :for="'checkbox-' + regiao.id" class="checkbox-label">{{ regiao.nome }}</label>
          </div>
        </div>
      </div>
      <button
        type="submit"
        :disabled="!isFormValid"
        :class="{'disabled-btn': !isFormValid}">
        Criar Promoção
      </button>
    </form>
    <div v-if="errorMessage" class="error-box">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script>
// import Multiselect from 'vue-multiselect';
import 'vue-multiselect/dist/vue-multiselect.min.css';

export default {
  name: 'AddPromocao',
  // components: { Multiselect },
  data() {
    return {
      novaPromocao: {
        nome_promocao: '',
        valor_promocao: '',
        data_inicio: '',
        data_fim: '',
        status: '',
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
  computed: {
    isFormValid() {
      return this.novaPromocao.nome_promocao &&
             this.novaPromocao.valor_promocao &&
             this.novaPromocao.data_inicio &&
             this.novaPromocao.data_fim &&
             this.novaPromocao.status &&
             this.novaPromocao.regioes.length > 0;
    }
  },
  methods: {
    // Busca as regiões do backend
    fetchRegioes() {
      fetch('http://localhost:5000/regioes')
        .then(response => response.json())
        .then(data => {
          this.regioes = data.map(regiao => ({
            id: regiao.id,
            nome: regiao.nome
          }));
        })
        .catch(error => {
          console.error('Erro ao carregar regiões:', error);
          this.errorMessage = 'Erro ao carregar regiões: ' + error.message;
        });
    },
    // Envia os dados da promoção para o backend
    adicionarPromocao() {
      const promocao = {
        nome_promocao: this.novaPromocao.nome_promocao,
        valor_promocao: this.novaPromocao.valor_promocao,
        data_inicio: this.novaPromocao.data_inicio,
        data_fim: this.novaPromocao.data_fim,
        status: this.novaPromocao.status,
        regioes_ids: this.novaPromocao.regioes.map(regiao => regiao) // Send as an array
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
            return response.json().then(err => {
              throw new Error(err.error);
            });
          }
          return response.json();
        })
        .then(() => {
          alert('Promoção criada com sucesso!');
          // Reseta os campos do formulário
          this.novaPromocao = {
            nome_promocao: '',
            valor_promocao: '',
            data_inicio: '',
            data_fim: '',
            status: '',
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

<style>
body {
  margin-left: 80px; /* Espaço para a barra lateral */
  background-color: rgb(249 250 251); /* Cor de fundo da página inteira */
}

.main-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem;
  background-color: rgb(249 250 251);
}

.form-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  width: 100%;
  max-width: 800px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.full-width {
  grid-column: span 2;
}

.label {
  font-weight: 600;
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
  text-align: left;
}

input,
select {
  width: 100%;
  padding: 12px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 6px;
  box-sizing: border-box;
}

button {
  padding: 12px;
  font-size: 16px;
  border: none;
  background-color: #007BFF;
  color: white;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  grid-column: span 2;
}

button:hover {
  background-color: #0056b3;
}

.error-box {
  color: red;
  margin-top: 20px;
  text-align: center;
}

/* Checkbox */

.checkbox-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start; /* Garante que os checkboxes fiquem sempre alinhados à esquerda */
}

.checkbox-item {
  display: flex;
  align-items: center;  /* Alinha verticalmente o checkbox e o texto */
  margin-right: 10px;
  background-color: rgb(243 244 246 / var(--tw-bg-opacity));
  border: 1px solid rgb(209 213 219 / var(--tw-border-opacity));
  border-radius: 0.25rem;
  padding: 5px 10px;
  flex-direction: row;  /* Coloca o texto à esquerda e o checkbox à direita */
  white-space: nowrap;  /* Impede que o texto quebre para a linha de baixo */
}

.checkbox-item input {
  margin-right: 8px;  /* Espaçamento entre o texto e o checkbox */
}

.checkbox-label {
  font-size: 14px;
  color: #333;
  cursor: pointer;  /* O cursor fica como um ponteiro para o clique */
}

.checkbox-item:hover {
  border-color: #007BFF;
}

.checkbox-item input:checked {
  background-color: #007BFF;
  border-color: #0056b3;
}

.checkbox-item input:checked + .checkbox-label {
  color: #007BFF;
}

/* Botão */
button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

button {
  padding: 12px;
  font-size: 16px;
  border: none;
  background-color: #007BFF;
  color: white;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover:not(:disabled) {
  background-color: #0056b3;
}

.disabled-btn {
  background-color: #ccc;
  cursor: not-allowed;
}

@media (max-width: 600px) {
  .form-container {
    grid-template-columns: 1fr;
  }
}
</style>
