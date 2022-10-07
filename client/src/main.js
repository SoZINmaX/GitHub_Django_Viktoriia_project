import { createApp } from 'vue'
import App from './App.vue'
import 'maz-ui/css/main.css'
import './assets/base.css'
import { createI18n } from 'vue-i18n'

const i18n = createI18n(App)
const app = createApp(App)

app.use(i18n)
app.mount('#app')
