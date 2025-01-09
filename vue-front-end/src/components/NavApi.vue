<template>
  <nav class="navbar navbar-expand-sm navbar-light bg-light">

    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item" v-for="(path)  in paths" :key="path.name">
          <router-link
              :to="path.path"
              v-bind:class="{'nav-link':true, 'active' : path.path === $route.fullPath}"
          >
            {{ path.name }}
          </router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>

export default {
  name: "NavApi",
  props: {
    paths: Array,
  },

}
</script>

<style scoped>
.nav-link{
  text-transform: capitalize;
}

</style>