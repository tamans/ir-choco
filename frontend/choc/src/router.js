import Search from "./components/SearchBar.vue"
import Results from "./components/Results.vue"
import Recs from "./components/Recs.vue"



import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    name: 'Search',
    component: Search,
    path: '/', 
  },
  {
    name: 'Results',
    component: Results,
    path: '/results', 
  },
  {
    name: 'Recs',
    component: Recs,
    path: '/recs', 
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;