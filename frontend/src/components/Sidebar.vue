<template>
  <div :class="['sidebar', { 'expanded': isExpanded }]">
    <ul>
      <!-- Ícone de Expansão/Contração -->
      <li @click="toggleSidebar" :class="{'selected': selectedSection === 'expand'}">
        <span class="menu-icon material-icons">
          {{ isExpanded ? 'chevron_left' : 'chevron_right' }}
        </span>
        <span v-if="isExpanded" class="menu-text"></span>
      </li>

      <!-- Exibição expandida -->
      <li v-if="isExpanded" @click="$emit('navigate', 'CreatePromotion')" :class="{'selected': selectedSection === 'CreatePromotion'}">
        <span class="menu-icon material-icons">add</span>
        <span class="menu-text">Criar Promoção</span>
      </li>
      <li v-if="isExpanded" @click="$emit('navigate', 'ListPromotions')" :class="{'selected': selectedSection === 'ListPromotions'}">
        <span class="menu-icon material-icons">list_alt</span>
        <span class="menu-text">Listar Promoções</span>
      </li>

      <!-- Exibição compactada -->
      <li v-if="!isExpanded" @click="$emit('navigate', 'CreatePromotion')" :class="{'selected': selectedSection === 'CreatePromotion'}">
        <span class="menu-icon material-icons">add</span>
      </li>
      <li v-if="!isExpanded" @click="$emit('navigate', 'ListPromotions')" :class="{'selected': selectedSection === 'ListPromotions'}">
        <span class="menu-icon material-icons">list_alt</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'SidebarMenu',
  data() {
    return {
      isExpanded: false, // Controle de expansão/compactação
      selectedSection: null // Armazena a seção selecionada
    };
  },
  methods: {
    toggleSidebar() {
      this.isExpanded = !this.isExpanded;
    }
  }
};
</script>

<style scoped>
/* Estilos principais da barra lateral */
.sidebar {
  width: 250px;
  background-color: white;
  padding: 10px;
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  transition: width 0.3s ease;
  z-index: 1000;
  overflow: hidden; /* Impede o texto de ultrapassar a largura da sidebar */
}

.sidebar.expanded {
  width: 200px;
}

.sidebar:not(.expanded) {
  width: 40px; /* Tamanho compactado */
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: flex;
  align-items: center;
  padding: 10px;
  cursor: pointer;
  border-bottom: 1px solid transparent;
}

li:hover, .selected {
  background-color: rgb(229, 231, 235); /* Cor do hover e seção selecionada */
}

.menu-text {
  font-size: 14px;
  margin-left: 10px;
  white-space: nowrap; /* Impede que o texto quebre a linha */
}

.menu-icon {
  font-size: 20px;
}

.toggle-btn {
  background-color: white;
  border: none;
  cursor: pointer;
  position: absolute;
  top: 10px;
  right: -25px;
  font-size: 20px;
}

.toggle-btn:hover {
  background-color: #ddd;
}

.expand-icon {
  color: rgb(55, 65, 81); /* Cor da seta */
}

/* Quando a barra lateral está compactada */
.sidebar:not(.expanded) .menu-text {
  display: none; /* Esconde os textos quando compactada */
}

.sidebar.expanded .menu-text {
  display: inline; /* Mostra os textos quando expandida */
}

/* Ajuste para a página começar após a barra */
body {
  margin-left: 250px; /* Espaço para a barra lateral */
}

.sidebar:not(.expanded) + .content {
  margin-left: 60px; /* Ajuste para a versão compactada */
}
</style>