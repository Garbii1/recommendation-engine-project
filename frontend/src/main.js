// src/main.js (add this line near the top)
import './assets/tailwind.css'

// ... rest of your main.js code
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')