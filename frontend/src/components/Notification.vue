<template>
  <div v-if="visible" class="notification" :class="type">
    <p>{{ message }}</p>
    <button @click="close">Close</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      visible: false,
      message: '',
      type: ''
    };
  },
  methods: {
    show(message, type) {
      this.message = message;
      this.type = type;
      this.visible = true;
      setTimeout(this.close, 5000); // Auto-close after 5 seconds
    },
    close() {
      this.visible = false;
    }
  }
};
</script>

<style scoped>
.notification {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.3);
}
.notification.success {
  background-color: #4caf50;
  color: white;
}
.notification.error {
  background-color: #f44336;
  color: white;
}
</style>
