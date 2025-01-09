<template>
  <tr>
    <th
        v-for="(info,field) in columns"
        :key="info.label"
        scope="col"
        :data-field="field"
        @click="sortField(field)"
    >
      {{ info.label }}
      <i
          v-bind:class="{
              'pi':true,
             // 'pi-':!this.sort.find((value) => value[field]),
              'pi-chevron-up':this.sort.find((value) => value[field])
                                    && this.sort.find((value) => value[field])[field] === 'asc',
              'pi-chevron-down':this.sort.find((value) => value[field])
                                    && this.sort.find((value) => value[field])[field] === 'desc',
              'disabled':true,
            }"
      />

    </th>
    <th scope="col" class="col-1 text-center col-xs-1">Actions</th>
  </tr>
</template>
<script>
export default {
  name: 'TableHeaderRow',
  props: {
    columns: Object,
  },
  methods: {
    sortField(field) {
      let sort = this.sort.find((value) => value[field])
      if (sort) {
        switch (sort[field]) {
          case 'asc':
            sort[field] = 'desc';
            break;
          case 'desc':
            delete sort[field];
            break;
          default:
            sort[field] = 'asc';
            break;
        }
      } else {
        sort = []
        sort[field] = 'asc'
        //this.sort.push(sort)
        this.sort=[sort]
      }
      console.log(this.sort)
      this.$emit('sortList', this.sort)
    },
  },
  data() {
    return {
      sort: []
    }
  }
}
</script>
<style scoped>
i {
  float: left;
  margin-top: 3px;
  margin-right: 3px;
  cursor: pointer;
}

</style>