<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
        <router-link class="navbar-brand" to="/" @click.native="resetState">Inicio</router-link>
        
        </div>
    </nav>
</template>
<script>
export default {
  methods: {
    resetState() {
      // Reset state of the web doing a page refresh
        window.location.reload();
    }
},
    name: 'NavbarComponent'
}

</script>