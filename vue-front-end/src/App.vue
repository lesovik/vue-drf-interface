<template>
  <div class="container">
    <NavApi :paths="routes"></NavApi>
    <RouterView :key="$route.path"/>
  </div>

</template>
<script>

import {computed, ref} from 'vue'
import NotFound from "@/components/NotFound.vue";
import NavApi from "@/components/NavApi.vue";

export default {
  name: 'App',
  components: {
    NavApi
  },
  watch: {
    $route(to) {
      let name = to.name ? this.capitalize(to.name) : null
      document.title = name || "Default Title";
    },
  },
  methods: {
    capitalize(val) {
      return String(val).charAt(0).toUpperCase() + String(val).slice(1);
    }
  },
  data() {
    return {
      routes: [],
      currentView: null
    }
  },
  created() {
    this.$router.options.routes.forEach(route => {
      this.routes.push({
        name: route.name,
        path: route.path
      })
    })
    const currentPath = ref(window.location.hash)

    window.addEventListener('hashchange', () => {
      currentPath.value = window.location.hash
    })
    this.currentView = computed(() => {
      return this.routes[currentPath.value.slice(1) || '/'] || NotFound
    })

  },
}
</script>
