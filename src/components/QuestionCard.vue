<template>
<div class="card flex">
    <div class="number">
        
        {{ question.question_id }}
    </div>
    <div class="title">
        {{ question.question.slice(3) }}
    </div>
    
</div>
</template>

<script setup>
import {defineProps} from "vue"

defineProps({
    question:Object
})
</script>

<style scoped>

</style>