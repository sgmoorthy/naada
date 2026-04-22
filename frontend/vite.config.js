import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react({
    babel: {
      plugins: [],
      babelrc: false,
      configFile: false
    }
  })],
  server: {
    port: 3000
  },
  // Base path matches the GitHub repo name for Pages deployment
  base: '/naada/',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    rollupOptions: {
      input: {
        main: './index.html'
      }
    }
  }
})
