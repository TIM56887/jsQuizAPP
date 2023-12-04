<script setup>
import { ref } from 'vue'

</script>

<template>
  <header class="p-3 md:p-4 border-b">
    <div class="text-gray-50 flex items-center">
      <div class="ps-1 w-1/2 text-xl md:ps-10 md:text-2xl md:w-5/12 font-semibold">
        <router-link to="/"><h1>JavaScript Quiz</h1></router-link>
        
      </div>
      <div class="text-right md:w-1/2 md:text-lg text-xs font-semibold hover:text-emerald-600">
        <h2><a href="/">#Timmy | Web Development Resources</a></h2>
      </div>
    </div>

  </header>
</template>

<style scoped>
</style>
