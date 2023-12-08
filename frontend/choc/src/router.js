import Search from "./Views/SearchView.vue"
import Results from "./Views/ResultsView.vue"
// import Recs from "./components/Recs.vue"
// import Bar from "./components/Bar.vue"



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
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;