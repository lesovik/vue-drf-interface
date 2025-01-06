<template>
  <ul class="pagination pagination-sm">
    <li class="page-item">
      <button
          class="page-link"
          type="button"
          @click="onClickFirstPage"
          v-bind:class="{'disabled':isInFirstPage}"
          :disabled="isInFirstPage"
      >
        &laquo;&laquo;
      </button>
    </li>
    <li class="page-item">
      <button
          class="page-link"
          type="button"
          @click="onClickPreviousPage"
          v-bind:class="{'disabled':isInFirstPage}"
          :disabled="isInFirstPage"
      >
        &laquo;
      </button>
    </li>
    <li
        class="page-item"
        v-for="page in pages"
        :key="page.name"
    >
      <button
          class="page-link"
          type="button"
          @click="onClickPage(page.name)"
          v-bind:class="{'active':page.name === currentPage}"
          :disabled="page.name === currentPage"
      >
        {{ page.name }}
      </button>
    </li>
    <li class="page-item">
      <button
          class="page-link"
          type="button"
          @click="onClickNextPage"
          v-bind:class="{'disabled':isInLastPage}"
          :disabled="isInLastPage"
      >
        &raquo;
      </button>
    </li>
    <li class="page-item">
      <button
          class="page-link"
          type="button"
          @click="onClickLastPage"
          v-bind:class="{'disabled':isInLastPage}"
          :disabled="isInLastPage"
      >
        &raquo;&raquo;
      </button>
    </li>
  </ul>
</template>

<script>
export default {
  name: 'ListPagination',
  emits: ['page-changed'],
  props: {
    maxVisibleButtons: {
      type: Number,
      required: false,
      default: 3
    },
    totalRecords: {
      type: Number,
      required: true
    },
    perPage: {
      type: Number,
      required: true
    },
    currentPage: {
      type: Number,
      required: true
    }
  },
  computed: {
    isInFirstPage() {
      return this.currentPage === 1;
    },
    isInLastPage() {
      return this.currentPage === this.totalPages;
    },
    totalPages() {
      return Math.ceil(this.totalRecords / this.perPage)
    },
    startPage() {
      if (this.currentPage === 1) {
        return 1;
      }
      if (this.currentPage === this.totalPages) {
        const start = this.totalPages - (this.maxVisibleButtons - 1);
        if (start === 0) {
          return 1;
        } else {
          return start;
        }
      }
      return this.currentPage - 1;
    },
    pages() {
      const range = [];
      for (
          let i = this.startPage;
          i <= Math.min(this.startPage + this.maxVisibleButtons - 1, this.totalPages);
          i++
      ) {
        range.push({
          name: i
        });
      }
      return range;
    },
  },
  methods: {
    onClickFirstPage() {
      this.$emit('page-changed', 1);
    },
    onClickPreviousPage() {
      this.$emit('page-changed', this.currentPage - 1);
    },
    onClickPage(page) {
      this.$emit('page-changed', page);
    },
    onClickNextPage() {
      this.$emit('page-changed', this.currentPage + 1);
    },
    onClickLastPage() {
      this.$emit('page-changed', this.totalPages);
    }
  }
}
</script>