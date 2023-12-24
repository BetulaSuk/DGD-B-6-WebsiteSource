import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue';
import RegisterView from '@/views/RegisterView.vue';
import LoginView from '@/views/LoginView.vue';
import DashboardView from '@/views/DashboardView.vue';
import ProfileView from '@/views/ProfileView.vue';
import NoteView from '@/views/NoteView.vue';
import EditNoteView from '@/views/EditNoteView.vue';

import SearchView from '@/views/SearchView.vue';
import ListView from '@/views/ListView.vue';
import store from '@/store'; // NEW

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  //add
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/list',
    name: 'ListView',
    component: ListView,
  },
  //add
  {
    path: '/register',
    name: 'RegisterView',
    component: RegisterView,
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
  },
  {
    path: '/dashboard',
    name: 'DashboardView',
    component: DashboardView,
    meta: { requiresAuth: true },
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: '/note/:id',
    name: 'NoteView',
    component: NoteView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/editnote/:id',
    name: 'EditNoteView',
    component: EditNoteView,
    meta: { requiresAuth: true },
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, _, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router
