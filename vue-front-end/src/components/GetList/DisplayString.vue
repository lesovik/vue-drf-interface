<script>
import moment from 'moment'

export default {
  name: 'DisplayString',
  props: {
    value:String,
    info: Object,
    editedRowId: Number
  },
  methods: {
    formatDate(value) {
      if (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
      }
    },
    formatChoice(){
      return this.info.choices.find(item => item.value === this.value).display_name
    },
  },
}
</script>
<template>
  <span v-if="info.type=='datetime'">
    {{ formatDate(value) }}
  </span>
  <span v-else-if="info.type=='choice'">
    {{ formatChoice(value)
    }}
  </span>
  <span v-else>
    {{ value }}
  </span>
</template>

<style scoped>

</style>