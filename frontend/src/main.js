import { createApp, useAttrs } from 'vue'
import App from './App.vue'
import router from '@/router/index.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import { createPinia } from 'pinia'
import 'bootstrap-icons/font/bootstrap-icons.css'
import { useThemeStore } from '@/stores/themeStore'

// In main.js or main.ts
import AOS from 'aos'
import 'aos/dist/aos.css'

const app = createApp(App)
app.use(createPinia())
const themeStore = useThemeStore()
themeStore.initializeTheme()
app.use(router)

AOS.init()
app.mount('#app')
