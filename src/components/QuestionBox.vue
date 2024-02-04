<template>
    <section>
        <div 
            class="md:container mx-auto mt-12 p-8 bg-white  lg:max-w-[768px] min-h-[700px] overflow-y-auto rounded-lg "
        >
            <!-- 操控當前題目的兩個按鈕 -->
            <div 
            v-if="!singleMode"
            class="grid grid-cols-10 h-[30px]">
                <button 
                    v-if="currentIndex != 0" 
                    @click="emit('previousQuestion')"
                    class="text-xl w-10 justify-self-end col-start-8 hover:text-2xl"><i class="bi bi-arrow-left-square"></i></button>
                <span class="text-center col-start-9">
                    {{ currentIndex+1 }} / {{ totalIndex }}
                </span>
                <button 
                    v-if="totalIndex != currentIndex+1" 
                    @click="emit('nextQuestion')" 
                    class=" text-xl hover:text-2xl w-10"><i class="bi bi-arrow-right-square"></i></button>
            </div>
            <!-- 題目的標題 -->
            <div class="text-2xl mb-2 font-bold" >
                {{ questionData.question }}
            </div>
            <!-- 題目的代碼 -->
            <div class="min-h-1/5 text-gray-50">
                <div class="bg-gray-600 text-xs rounded-t-md ps-3 py-1">javascript</div>
                <pre class="bg-slate-950 rounded-b-md px-10 py-3 overflow-x-auto"><code>{{ questionData.question_code }}</code></pre>
            </div>
            <!-- 題目的選項 -->
            <div class="h-2/5 flex flex-col">
                <OptionButton 
                    v-for="option, index in options" :key="index"
                    :option="option"
                    :index="index"
                    :answers="questionData.answer"
                    @answerChecked="showExplanationPage"
                />
            </div>
            <!-- 在獲取五個題目的按鈕，做完所有題目時要顯示 -->
            <div class="flex justify-center">
                <button
                    v-if="totalIndex === currentIndex+1" 
                    class="border rounded-md bg-emerald-600 text-gray-50 hover:bg-emerald-900 text-3xl p-3 mt-10" 
                    @click="getfiveQuestion"
                > 
                        5 more questions <i class="ms-2 text-3xl bi bi-cloud-download"></i>
                </button>
            </div>
        </div>
        <!-- 題目的解答，選對答案時要顯示 -->
        <transition name="fade">  
            <div v-if="showExplanation" 
                class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2
                       flex flex-col justify-between p-8  
                       max-w-[500px] min-h-[500px] max-h-[600px]
                       bg-white rounded-lg"
                        >
                <div class="flex items-center justify-center text-4xl text-center pt-2 font-semibold h-1/5 flex-2">
                    Correct!
                    <i class="bi bi-check-circle text-center text-6xl text-emerald-500 leading-3"></i></div>
                <div v-if="totalIndex !== currentIndex+1" class="text-2xl text-center">You finished! </div>
                <div class="text-2xl font-semibold flex-1 overflow-y-auto">
                    Explanation:
                    <div class="explantion text-base font-medium"> {{ questionData.explanation }}</div>
                </div>
                <div class="flex-2 flex justify-between mt-10">
                    <button  @click="closeExplanationPage" class="border rounded-md  bg-slate-500 text-gray-50 hover:bg-slate-400 text-xl w-1/3 self-end py-1">close</button>
                    <button v-if="totalIndex !== currentIndex+1" @click="nextQuestion" class="border rounded-md  bg-slate-500 text-gray-50 hover:bg-slate-400 text-xl w-1/3 self-end py-1">next</button>                   
                </div>
            </div>
        </transition>
    </section>
</template>

<script setup>
import OptionButton from './OptionButton.vue'
import { ref, toRefs, onMounted, computed,reactive, toRef, defineProps, watch} from "vue"

let showExplanation = ref(false);
let totalIndex = ref(5);
let finsihedAllQuestions = ref(false);
// const props = defineProps(['questionData','currentIndex','singleMode']);
const props = defineProps({
    questionData:{
        type:Object
    },
    currentIndex:{
        type:Number,
        default:0
    },
    singleMode:{
        type:Boolean,
        default:false
    }
})
const emit = defineEmits(['nextQuestion','previousQuestion']);

let options  = computed(()=>{
        return[props.questionData.option1,props.questionData.option2,props.questionData.option3,props.questionData.option4];
})
function showExplanationPage(){
    showExplanation.value = true;
}
function closeExplanationPage(){
    showExplanation.value = false;
}
function nextQuestion(){
    closeExplanationPage();
    emit('nextQuestion');
}



</script>

<style scoped>
    .fade-enter-active,
    .fade-leave-active {
        transition: opacity 0.2s ease;
    }

    .fade-enter-from,
    .fade-leave-to {
        opacity: 0; 
    }

</style>