import { createRouter, createWebHashHistory  } from 'vue-router';
import HomePage from './pages/HomePage.vue'
import Question from './pages/Question.vue'
import QuestionList from './pages/QuestionList.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/question', component: Question },
  { path: '/questionlist', component:QuestionList}
  
]

export default createRouter({
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
  })

