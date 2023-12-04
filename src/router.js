import { createRouter, createWebHistory } from 'vue-router';
import JsQuiz from './pages/JsQuiz.vue'
import Home from './pages/Home.vue'

// const Home = { template: NavBar }
// const About = { template: '<div>About</div>' }
const routes = [
  { path: '/jsquiz', component: JsQuiz },
  { path: '/', component: Home },
]

export default createRouter({
    history: createWebHistory(),
    routes, // short for `routes: routes`
  })

