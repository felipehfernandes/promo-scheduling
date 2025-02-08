<template>
  <div class="upper-bar">
    <ul>
      <li @click="$emit('navigate', 'CreatePromotion')">Criar Promoção</li>
      <li @click="$emit('navigate', 'ListPromotions')">Listar Promoções</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'UpperBarMenu'
};
</script>

<style scoped>
.upper-bar {
  width: 100%;
  background-color: #f4f4f4;
  padding: 10px;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
  display: flex;
  justify-content: center;
}
ul {
  list-style-type: none;
  padding: 0;
  display: flex;
  gap: 20px;
}
li {
  padding: 10px;
  cursor: pointer;
  border-bottom: 1px solid transparent;
}
li:hover {
  border-bottom: 1px solid #ccc;
}
</style>
