<script setup>
import { ref } from 'vue'

</script>

<template>
  <header class="p-3 md:p-4 border-b">
    <div class="text-gray-50 flex items-center">
      <div class="ps-1 w-1/2  md:ps-10  md:w-5/12 flex">
        <router-link to="/"><h1 class="md:text-2xl text-xl font-semibold">JavaScript Quiz</h1></router-link>
      </div>
      <div class="text-right md:w-1/2 md:text-lg text-xs font-semibold ">
        <span class="hover:text-emerald-600"><a href="/">#Timmy | Web Development Resources</a></span>
      </div>
    </div>

  </header>
</template>

<style scoped>
</style>
