<template>
  <div class="dropdown boostrap-select" :class="{'open' : open}">
    <input
        type="text"
        v-bind:class="{
              'form-control':true,
            }"
        v-model="searchValue.label"
        @input="searchChanged"
        @keydown.enter="suggestionSelected(matches[highlightIndex])"
        @keydown.down="down"
        @keydown.up="up"
    />
    <span class="toggle" @mousedown.prevent @click="setOpen(!open)">
      <span class="arrow-up pi pi-arrow-circle-up"></span>
      <span class="arrow-down pi pi-arrow-circle-down"></span>
    </span>
    <ul class="suggestion-list dropdown-menu">
      <li
          v-for="(suggestion, index) in matches"
          class="inner show dropdown-item"
          :key="suggestion.id"
          :class="{'active' : index === highlightIndex}"
          @mousedown.prevent
          @click="suggestionSelected(suggestion)"
      >
        {{ suggestion.label }}
      </li>
    </ul>
  </div>
</template>

<script>
import ApiSettings from "@/ApiSettings.vue";

export default {
  name: 'InputSearchSelect',
  props: {
    field: String,
    value: Object,
    info: Object,
  },
  computed: {
    matches() {
      let optionArray = []
      this.options.forEach((option) => {
            optionArray.push(option);
          }
      )

      return optionArray.filter((option) => {
        let optionText = option.label.toUpperCase()
        return optionText.match(this.searchValue.label.toUpperCase())
      })
    }
  },
  watch: {
    value: function (newValue) {
      this.updateComponentWithValue(newValue)
    }
  },
  mounted() {
    this.options.push(this.getSearchValue())
    this.updateComponentWithValue(this.value)
  },
  methods: {
    setOpen(isOpen) {
      this.open = isOpen
    },
    searchChanged() {
      if (!this.open) {
        this.open = true
      }
      this.fetchData()
      this.highlightIndex = 0
    },
    suggestionSelected(suggestion) {
      this.open = false
      this.searchValue = Object.assign({}, suggestion)
      this.$emit('input', suggestion)
    },
    updateComponentWithValue(newValue) {
      if (Object.values(this.options).indexOf(newValue) > -1) {
        for (let option in this.options) {
          if (option.label === newValue.label) {
            this.searchValue = Object.assign({}, newValue)
          }
        }
      }
    },
    up() {
      if (this.open) {
        if (this.highlightIndex > 0) {
          this.highlightIndex--
        }
      } else {
        this.setOpen(true)
      }
    },
    down() {
      if (this.open) {
        if (this.highlightIndex < this.matches.length - 1) {
          this.highlightIndex++
        }
      } else {
        this.setOpen(true)
      }
    },
    async fetchData() {
      this.options = await fetch(ApiSettings.rootUrl + this.field + '/?search=' + this.searchValue.label)
          .then(async response => {
            let data = await response.json();
            return data.results
          })
          .catch((err) => {
            console.error(err);
          });
    },
    getSearchValue(){
      if(this.value){
        return Object.assign({}, this.value)
      }
      return {id:null,label:''}
    }
  },
  data() {
    return {
      searchValue: this.getSearchValue(),
      selectedOption: null,
      open: false,
      highlightIndex: 0,
      options: []
    }
  },

}
</script>
<style scoped>
.dropdown {
  display: inline-block;
  position: relative;
}

.suggestion-list {
  background-color: rgba(255, 255, 255, 0.95);
  border: 1px solid #ddd;
  list-style: none;
  display: block;
  margin: 0;
  padding: 0;
  width: 100%;
  overflow: hidden;
  position: absolute;
  top: 40px;
  left: 0;
  z-index: 2;
}

.dropdown.open .suggestion-list {
  display: block;
}

.dropdown .suggestion-list {
  display: none;
}

.toggle {
  position: absolute;
  right: 8px;
  top: 8px;
}

.toggle .arrow-up {
  display: none;
}

.open .toggle .arrow-up {
  display: inline-block;
}

.open .toggle .arrow-down {
  display: none;
}

.suggestion-list li {
  cursor: pointer;
}

.suggestion-list li:hover {
  color: #fff;
  background-color: #ccc;
}

.active {
  color: #fff;
  background-color: #42b983;
}
</style>