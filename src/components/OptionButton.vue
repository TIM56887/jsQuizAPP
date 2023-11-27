<template>
    <button 
    :class="{shake:shaking}"
    class="h-12 mt-4 flex items-center border rounded-md border-black hover:bg-slate-200"
    @click="checkAnswer" 
    >
                <div class="index w-9 text-base">{{ index +1 }} </div>
                <div class="option text-xl">{{ option }}</div>
    </button>
</template>

<script setup>

import { ref, defineProps} from "vue" 
const props= defineProps({
    index:Number,
    option:String,
    answer:Number
})

const emit = defineEmits(['answerChecked'])
let shaking = ref(false)
function checkAnswer () {
    if (props.index !== props.answer) {
        shaking.value = true
        setTimeout(()=> shaking.value = false,500);
    }else {
        emit('answerChecked',props.index)
    }

    
}
</script>

<style scoped>
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  50% { transform: translateX(5px); }
  75% { transform: translateX(-5px); }
}

.shake {
  animation: shake 0.4s; 
}
</style>