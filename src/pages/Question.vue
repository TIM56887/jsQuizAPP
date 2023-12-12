<template>
    <section>


        <div 
            v-if="questions.length > 0"  
            class="md:container mx-auto mt-12 p-8 bg-white  lg:max-w-[768px] min-h-[700px] overflow-y-auto rounded-lg "
        >
            <div class="grid grid-cols-10 h-[30px]">
                <button v-if="index!=0" @click="index--" class="text-xl w-10 justify-self-end col-start-8 hover:text-2xl"><i class="bi bi-arrow-left-square"></i></button>
                <span class="text-center col-start-9">
                    {{ index +1 }} / {{ questions.length }}
                </span>
                <button v-if="questions.length > index+1" @click="index++" class=" text-xl hover:text-2xl w-10"><i class="bi bi-arrow-right-square"></i></button>
            </div>
            <div class="text-2xl mb-2 font-bold" >
                {{questions[index].question}}
            </div>
            <div class="min-h-1/5 text-gray-50">
                <div class="bg-gray-600 text-xs rounded-t-md ps-3 py-1">javascript</div>
                <pre class="bg-slate-950 rounded-b-md px-10 py-3 overflow-x-auto"><code>{{ questions[index].question_code }}</code></pre>
            </div>
            <div class="h-2/5 flex flex-col">
                <OptionButton 
                    v-for="option, index in currentOption" :key="index"
                    :option="option"
                    :index="index"
                    :answers="answer"
                    @answerChecked="showExplanationPage"
                />
            </div>
            <div class="flex justify-center">
                <button
                    v-if="finsihed" 
                    class="border rounded-md bg-emerald-600 text-gray-50 hover:bg-emerald-900 text-3xl p-3 mt-10" 
                    @click="getfiveQuestion"
                > 
                        5 more questions <i class="ms-2 text-3xl bi bi-cloud-download"></i>
                </button>
            </div>
        </div>
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
                <div v-if="finsihed" class="text-2xl text-center">You finished! </div>
                <div class="text-2xl font-semibold flex-1 overflow-y-auto">
                    Explanation:
                    <div class="explantion text-base font-medium"> {{ questions[index].explanation }}</div>
                </div>
                <div class="flex-2 flex justify-between mt-10">
                    <button  @click="closeExpanation" class="border rounded-md  bg-slate-500 text-gray-50 hover:bg-slate-400 text-xl w-1/3 self-end py-1">close</button>
                    <button v-if="!finsihed" @click="nextQuestion" class="border rounded-md  bg-slate-500 text-gray-50 hover:bg-slate-400 text-xl w-1/3 self-end py-1">next</button>                   
                </div>
            </div>
        </transition>
    </section>
</template>

<script setup>
import OptionButton from '../components/OptionButton.vue'
import { ref, toRefs, onMounted, computed,reactive, toRef} from "vue"

let data = reactive({
    questions:[],
    index:0,
    showExplanation:false,
    finsihed:false,
    test:'123'
})
let {questions, index, showExplanation,finsihed} = toRefs(data)

let answer = computed(()=> questions.value[index.value].answer)
let currentOption = computed(() => {
  if (questions.value.length > 0 && index.value >= 0 && index.value < questions.value.length) {
    const currentQuestion = questions.value[index.value];
    if (currentQuestion) {
      return [currentQuestion.option1, currentQuestion.option2, currentQuestion.option3, currentQuestion.option4];
    }
  }
  return []; 
});
const xhr = new XMLHttpRequest();

let isSending = false;
onMounted(()=>{

    if (isSending) {
        xhr.abort()
    }
    isSending = true;
    xhr.open("GET", "/quiz?amount=5&listed=false", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            isSending = false;
            if (xhr.status === 200) {
                questions.value = JSON.parse(xhr.responseText);
        } else {
            console.error(xhr.statusText);
         }
        }
    };
    xhr.onerror = function () {
        console.error(xhr.statusText);
    };
    
    xhr.send();}
    )
const getfiveQuestion = () => {
    const currentQuestionIds = questions.value.map(q => q.question_id);

    xhr.open("POST", "/fivequiz", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                questions.value.push(...JSON.parse(xhr.responseText));
                finsihed.value = false
                index.value++;
            } else {
                console.error(xhr.statusText);
            }
        }
    };

    xhr.send(JSON.stringify({ currentQuestionIds }));
};
const showExplanationPage = () => {
    if (questions.value.length  > index.value + 1){
        showExplanation.value = true
        
    }else{
        showExplanation.value = true
        finsihed.value = true
        
    }
}
const nextQuestion = () => {
    showExplanation.value = false
    index.value++
}
const closeExpanation = () => showExplanation.value = false


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