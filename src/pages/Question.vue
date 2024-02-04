<template>
    <section>
        <QuestionBox
            v-if="finsihedFetching" 
            :questionData="questions[currentIndex]"
            :currentIndex="currentIndex"
            @nextQuestion="nextQuestion"
            @previousQuestion="previousQuestion"
        />
    </section>
</template>

<script setup>
import QuestionBox from '../components/QuestionBox.vue';
import { ref, toRefs, onMounted, computed,reactive, toRef} from "vue"

let finsihedFetching = ref(false);
let questions = ref([]);
let currentIndex = ref(0)

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
                finsihedFetching.value = true;
        } else {
            console.error(xhr.statusText);
         }
        }
    };
    xhr.onerror = function () {
        console.error(xhr.statusText);
    };
    xhr.send();
}
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

const nextQuestion = () => {
    currentIndex.value ++;
}
const previousQuestion = ()=> {
    currentIndex.value --;
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