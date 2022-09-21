import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CommentView from '../views/CommentView.vue'
import ClientView from '../views/ClientView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/leave_comment',
      name: 'leave_comment',
      component: CommentView
    },
    {
      path: '/client',
      name: 'client',
      component: ClientView
    },
  ]
})

export default router
