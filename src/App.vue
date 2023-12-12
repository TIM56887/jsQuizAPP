<script setup>
import NavBar from './components/NavBar.vue';
</script>

<template>
  <NavBar />

  <router-view v-slot="{ Component }">
    <transition name="fade">
      <component :is="Component"></component>
    </transition>
  </router-view>
  
  
</template>

<style scoped>
.fade-enter-active {
  transition: opacity 0.3s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
