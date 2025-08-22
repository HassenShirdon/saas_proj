import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { createPinia } from "pinia";
import PrimeVue from "primevue/config";
// import "primevue/resources/themes/lara-light-blue/theme.css";
import "primeicons/primeicons.css";
import "./assets/tailwind.css";

const app = createApp(App);
app.use(router);
app.use(createPinia());
app.use(PrimeVue);
app.mount("#app");
