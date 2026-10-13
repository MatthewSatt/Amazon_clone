import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// In development the React app runs on :3000 and proxies API calls to Flask
const api = `http://localhost:${process.env.API_PORT || 8000}`

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: { '/api': api },
  },
})
