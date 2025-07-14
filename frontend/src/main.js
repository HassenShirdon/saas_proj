import { createApp, useAttrs } from 'vue'
import App from './App.vue'
import router from '@/router/index.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import { createPinia } from 'pinia'
import 'bootstrap-icons/font/bootstrap-icons.css'

// In main.js or main.ts
import AOS from 'aos'
import 'aos/dist/aos.css'

const app = createApp(App)
app.use(createPinia())
app.use(router)

AOS.init()
app.mount('#app')
