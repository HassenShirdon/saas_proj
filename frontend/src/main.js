import { createApp, useAttrs } from 'vue'
import App from './App.vue'
import router from '@/router/index.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import 'bootstrap-icons/font/bootstrap-icons.css'
// In main.js or main.ts
import AOS from 'aos'
import 'aos/dist/aos.css'
import { createPinia } from 'pinia'

const app = createApp(App)
app.use(router)
app.use(createPinia())
AOS.init()
app.mount('#app')
