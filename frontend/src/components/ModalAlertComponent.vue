<template>
  <div class="modal-overlay" v-if="show">
    <div class="card modal-card">
      <div class="card-header modal-header">
        <h3>{{ title }}</h3>
        <button @click="hideModal" class="btn-close"/>
      </div>
      <div class="card-body modal-body">
        <slot></slot>
      </div>
      <div class="card-footer modal-footer">
        <button @click="hideModal" class="btn btn-dark">Entendido</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: {
      type: Boolean,
      required: true
    },
    title: {
      type: String,
      default: 'Atención'
    }
  },
  methods: {
    hideModal() {
      this.$emit('update:show', false);
    }
  }
};
</script>

<style scoped>
/* Tus estilos aquí */
.modal-overlay {
  z-index: 999999;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-card {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  max-width: 500px;
  width: 100%;
}

.btn-close {
  float: right;
  border: none;
  background-color: transparent;
  font-size: 1.2rem;
}

.card-header,
.card-body,
.card-footer {
  padding: 1em;
}

.card-footer {
  text-align: right;
}
</style>