<template>
    <section class="md:container mx-auto  p-8 bg-white  lg:max-w-[768px] rounded-lg relative" v-if="questions.length != 0">
        <div class="pagebox grid grid-cols-3 w-20">
            <button v-if="index!=0" @click="index--" class="text-xl w-10"><i class="hover:bg-slate-200 bi bi-arrow-left-square"></i></button>
            <button v-if="questions.length > index+1" @click="index++" class=" text-xl col-start-2 w-10"><i class="hover:bg-slate-200 bi bi-arrow-right-square"></i></button>
        </div>
        <div class="text-2xl mb-2 font-bold" ><span>{{ index+1 }}. </span>{{questions[index].question}}</div>
        <div class="h-1/5"><pre class="bg-slate-500 rounded-lg text-gray-50"><code>{{ questions[index].question_code }}</code></pre></div>
        <div class="answerbar h-2/5 flex flex-col">
            <!-- <button
                v-for="option, index in currentOption"
                :key="index" 
                :class="{shake:shaking}"
                class="h-12 mt-4 flex items-center border rounded-md border-black hover:bg-slate-200" 
                @click="checkAnswer(index)"
                >
                <div class="index w-9 text-base">{{ index+1 }} </div>
                <div class="option text-xl">{{ option }}</div>
                
            </button> -->
            <OptionButton 
            v-for="option, index in currentOption" :key="index"
            :option="option"
            :index="index"
            :answer="questions[index].answer"
            @answerChecked="showExplanationPage"

            />
        </div>
        
        <div class="explanation absolute inset-0 mx-auto bg-white rounded-lg max-w-[500px] flex flex-col justify-between p-8" v-if="showExplanation">
            <div class="text-5xl text-center pt-2">Correct!</div>
            <div v-if="finsihed" class="text-2xl text-center">You finished! </div>
            <div class="text-2xl">Explanation:<div class="explantion text-base"> {{ questions[index].explanation }}</div></div>
            <button v-if="!finsihed" @click="nextQuestion" class="border rounded-md border-black bg-slate-500 text-gray-50 hover:bg-slate-400 text-xl w-1/3 self-end">next</button>
            <button v-if="finsihed" @click="closeExpanation" class="border rounded-md border-black bg-slate-500 text-gray-50 hover:bg-slate-400 text-xl w-1/3 self-end">close</button>
        </div>
        
    </section>
</template>

<script setup>
import OptionButton from './OptionButton.vue'
import { ref, toRefs, onMounted, computed,reactive} from "vue" 
let xhr = new XMLHttpRequest();
let data = reactive({
    questions:[],
    index:0,
    showExplanation:false,
    finsihed:false,
    shaking:false
})
let {questions, index, showExplanation,finsihed, shaking} = toRefs(data)

let currentOption = computed(() => {
  // 确保数组不为空且索引在有效范围内
  if (questions.value.length > 0 && index.value >= 0 && index.value < questions.value.length) {
    const currentQuestion = questions.value[index.value];
    // 确保当前问题已定义
    if (currentQuestion) {
      return [currentQuestion.option1, currentQuestion.option2, currentQuestion.option3, currentQuestion.option4];
    }
  }
  return []; // 如果条件不满足，返回空数组
});
onMounted(()=>{
    xhr.open("GET", "/quiz", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                data.questions = JSON.parse(xhr.responseText);

        } else {
            console.error(xhr.statusText);
         }
        }
    };
    xhr.onerror = function (e) {
        console.error(xhr.statusText);
    };
    xhr.send(null);}
    
    )

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


</style>