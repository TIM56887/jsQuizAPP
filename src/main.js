import { createApp } from 'vue'
import router from './router.js'
import './style.css'
import App from './App.vue'
import axios from 'axios'
import 'bootstrap-icons/font/bootstrap-icons.css';

const Home = { template: '<div>Home</div>' }
const About = { template: '<div>About</div>' }


const app =createApp(App)
app.use(router);
app.mount('#app');

