import {createRouter, createWebHistory} from 'vue-router'
import GetList from './components/GetList.vue'
import GetDetail from './components/GetDetail.vue'
import ApiSettings from "@/ApiSettings.vue";

let responseData = await fetch(ApiSettings.rootUrl)
    .then(async response => {
        return await response.json();
    })
    .catch((err) => {
        console.error(err);
    });
let routes = []

routes.push({
    path: '/',
    component: GetList,
    name: 'Home',
    props: {
        'url': Object.values(responseData)[0],
        'title': Object.keys(responseData)[0]
    }
})
Object.keys(responseData).forEach(title => {
    routes.push({
        path: '/' + title,
        name: title.replace('_', ' '),
        component: GetList,
        props: {'url': responseData[title], 'title': title.replace('_', ' ')},

    })

})
const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router