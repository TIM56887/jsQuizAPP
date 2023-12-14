<template>
    <button 
        :class="wrongAnswer"
        class="min-h-[48px] mt-4 flex items-center border-2 border-stone-300 rounded-md hover:bg-slate-200 overflow-auto"
        @click="checkAnswer" 
    >
                <div class="index w-9 text-base">{{ index +1 }} </div>
                <div class="option text-xl">{{ option.substring(3) }}</div>
    </button>
</template>

<script setup>

import { ref, defineProps, reactive} from "vue" 

let wrongAnswer = reactive({
    shake:false,
    'border-red-600':false

})
const props= defineProps({
    index:Number,
    option:String,
    answers:Number
})
const emit = defineEmits(['answerChecked'])

function checkAnswer () {
    if (props.index !== props.answers) {
        wrongAnswer.shake = true
        wrongAnswer['border-red-600'] = true
        setTimeout(()=> {
            wrongAnswer.shake = false;
            wrongAnswer['border-red-600'] =false;
        },500);
    }else {
        emit('answerChecked',props.index);
        

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