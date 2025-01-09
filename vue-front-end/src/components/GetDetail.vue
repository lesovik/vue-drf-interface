<script>
export default {
  name: "GetDetail",
  props: {
    title: String,
    url: String
  },
}
</script>

<template>
<h1>{{ title }}</h1>
  <h2>{{ $route.params.id }}</h2>
</template>

<style scoped>

</style>