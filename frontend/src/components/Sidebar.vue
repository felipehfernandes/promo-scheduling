<template>
  <div class="sidebar">
    <ul>
      <li @click="$emit('navigate', 'CreatePromotion')">Criar Promoção</li>
      <li @click="$emit('navigate', 'ListPromotions')">Listar Promoções</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'SidebarMenu'
};
</script>

<style scoped>
.sidebar {
  width: 200px;
  background-color: #f4f4f4;
  padding: 10px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  padding: 10px;
  cursor: pointer;
  border-bottom: 1px solid #ccc;
}
li:hover {
  background-color: #ddd;
}
</style>
