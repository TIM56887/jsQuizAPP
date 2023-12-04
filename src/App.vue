<script setup>
import NavBar from './components/NavBar.vue';
</script>

<template>
  <NavBar />
  <transition name="fade">
    <router-view></router-view>
  </transition>
  
  
</template>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter, .fade-leave-active {
  opacity: 0.1;
}
</style>
