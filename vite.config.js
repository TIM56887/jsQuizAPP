import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      // 代理请求
      '/quiz': {
        target: 'http://127.0.0.1:5000', // 目标服务器
        changeOrigin: true, // 允许改变源
        secure: false, // 如果是https接口，需要配置这个参数
      },
      '/fivequiz': {
        target: 'http://127.0.0.1:5000', // 目标服务器
        changeOrigin: true, // 允许改变源
        secure: false, // 如果是https接口，需要配置这个参数
      },
    }
  }
})

