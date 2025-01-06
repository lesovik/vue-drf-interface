<template>
  <h1>{{ title }}</h1>
  <div v-if="data && options">
    <ListPagination
        :totalRecords="data.count"
        :perPage="data.page_size"
        :currentPage="currentPage"
        @page-changed="onPageChange"
    />
    <div class="btn-group btn-group-xs float-end list-buttons" role="group">
      <button class="btn btn-xs btn-outline-primary" @click="refresh()">
        <i class="pi pi-search"></i>
      </button>
      <button class="btn btn-xs btn-outline-primary" @click="refresh()">
        <i class="pi pi-refresh"></i>
      </button>
      <button class="btn btn-xs btn-success" @click="addRow(options.actions.POST)">
        <i class="pi pi-plus"></i>
      </button>
    </div>
    <table
        class="table table-hover"
        data-toggle="table"
        data-classes="table table-striped">
      <thead class="table-primary">
      <TableHeaderRow
          :columns="options.actions.POST"
          @sortList="sortList = $event;refresh()"
      />
      </thead>
      <tbody v-if="rows.length>0">
      <TableRow
          v-for="(item,index) in rows"
          :key="index"
          :rowData="item.row"
          :index="index"
          :url="this.url"
          :tEdit="item.toggleEdit"
          :options="options.actions.POST"
      />
      </tbody>
    </table>
    <ListPagination
        :totalRecords="data.count"
        :perPage="data.page_size"
        :currentPage="currentPage"
        @page-changed="onPageChange"
    />
  </div>

</template>

<script>
import {isProxy, toRaw} from 'vue';
import TableHeaderRow from './GetList/TableHeaderRow.vue'
import TableRow from './GetList/TableRow.vue'
import ListPagination from "@/components/GetList/ListPagination.vue";

export default {
  name: 'GetList',
  emits: ['page-changed'],
  props: {
    title: String,
    url: String
  },
  components: {
    TableHeaderRow,
    TableRow,
    ListPagination,

  },
  watch: {
    url: function () { // watch it
      this.refresh()
    }
  },
  data() {
    return {
      data: null,
      options: null,
      index: null,
      currentPage: 1,
      rows: [],
      sortList: null,
    };
  },
  created() {
    this.refresh()
  },

  methods: {
    getRows() {
      let arr = []
      this.data.results.forEach(function (row, index) {
        arr.push(
            {'index': index, 'row': row, 'toggleEdit': false}
        )
      })
      return arr
    },
    addRow(fields) {
      let newRow = {}
      let rawData = fields;
      if (isProxy(rawData)) {
        rawData = toRaw(rawData)
      }
      for (let key of Object.keys(rawData)) {
        newRow[key] = null
      }
      this.index++
      this.rows.push({'index': this.index, 'row': newRow, 'toggleEdit': true})

    },
    removeRow(index) {
      this.rows.splice(index, 1)
    },
    refresh() {
      this.fetchOptions()
      this.fetchData()
    },
    getUrl() {
      let query = '?page=' + this.currentPage
      if (this.sortList) {
        this.sortList.forEach((column) => {
          let key = Object.keys(column)[0]
          if (key) {
            query += '&sort_' + key + '=' + column[key]
          }
        })
      }
      return this.url + query
    },
    async fetchData() {
      fetch(this.getUrl())
          .then(async response => {
            this.data = await response.json();
            this.rows = this.getRows()
          })
          .catch((err) => {
            console.error(err);
          });
    },
    async fetchOptions() {
      fetch(this.url, {
        method: 'OPTIONS'
      })
          .then(async response => {
            this.options = await response.json();
          })
          .catch((err) => {
            console.error(err);
          });
    },
    async onPageChange(page) {
      this.currentPage = page;
      await this.fetchData()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.pagination {
  float: left
}

h1 {
  text-transform: capitalize;
}
</style>
