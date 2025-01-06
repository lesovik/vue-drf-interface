<script>
export default {
  name: 'DisplayNumber',
  props: {
    value:Number,
    info: Object,
  },
}
</script>
<template>
  <span>
    {{ value }}
  </span>
</template>

<style scoped>

</style>