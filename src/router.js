import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './pages/HomePage.vue'
import Question from './pages/Question.vue'
import QuestionList from './pages/QuestionList.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/question', component: Question },
  { path: '/questionlist', component:QuestionList}
  
]

export default createRouter({
    history: createWebHistory('/jsquiz/'),
    routes, // short for `routes: routes`
  })

