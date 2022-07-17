import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from '../views/HomeView.vue';
import Job from '../views/Job.vue';
import JobEditor from '../views/JobEditor.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/job/:id',
    name: 'job',
    component: Job,
    props: true,
  },
  {
    path: '/editor',
    name: 'editor',
    component: JobEditor,
    props: true,
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
