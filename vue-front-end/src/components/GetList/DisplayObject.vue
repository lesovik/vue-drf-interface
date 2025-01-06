<script>
export default {
  name: 'DisplayObject',
  props: {
    value:Object,
    info: Object,
  },
}
</script>
<template>
  <span>
    {{ value[Object.keys(value)[1]] }}
  </span>
</template>

<style scoped>

</style>