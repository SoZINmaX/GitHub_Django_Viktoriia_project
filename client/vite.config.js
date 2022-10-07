import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import vueI18n from '@intlify/vite-plugin-vue-i18n'


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(),
    vueI18n({
      compositionOnly: true
    }),
  [
    'component',
    {
      libraryName: 'maz-ui',
      styleLibraryName: 'css'
    }
  ]
],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server:{
    port: 5173,
    host: '0.0.0.0',
    watch: {
        usePolling: true
    }
  }
})
