// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RecommendationsView from '../views/RecommendationsView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/recommendations',
    name: 'recommendations',
    component: RecommendationsView
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  // BEFORE:
  // history: createWebHistory(import.meta.env.BASE_URL),

  // AFTER:
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router