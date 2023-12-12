<template>
    <section>
        <div class="lg:container mx-auto bg-slate-400 max-w-[1000px]">
            <div><h1 class="text-3xl font-semibold text-slate-50">Question List</h1></div>
            <div>
                <QuestionCard 
                    v-for="question in questionList"
                    :question="question"  
                />
            </div>
            


        </div>
    </section>
</template>

<script setup>

import { reactive, ref} from 'vue'
import QuestionCard from '../components/QuestionCard.vue';
import axios from 'axios'

let questionList = ref([])

axios({
    url:'/quiz',
    method:'get',
    responseType:'json',
    params:{
        amount:10,
        listed:true
    }
    
}).then((res)=>{
    questionList.value = res.data
    console.log(questionList)
})


</script>

<style scoped>
</style>