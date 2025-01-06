<template>
  <tr>
    <td

        v-for="(props,field) in options"
        :key="field" class="align-middle"
        nowrap="nowrap"
        v-bind:class="{
          'col-1 col-integer': field==='id',
          'col-4': props.type==='string',
          'col-2': props.type==='choices',
          'col-2': props.type==='nested object',
          'col-1': props.type==='datetime',
          'was-validated' : !errors[field] && blurred[field]
        }"
    >
      <template v-if="!props.read_only && toggleEdit">
        <input
            v-if="props.type==='string'"
            type="text"
            :id="field + '_' + index"
            v-model="row[field]"
            class="form-control"
            v-bind:class="{
              'form-control':true,
              'is-invalid' : errors[field] && blurred[field]
            }"
            v-on:blur="blurred[field] = true; this.isValid(field,row[field])"
            v-on:focus="blurred[field] = false"
            v-on:change="errors[field] = false"
        >
        <select
            v-else-if="props.type==='choice'"
            v-model="row[field]"
            class="form-select"
            v-bind:class="{'form-control':true, 'is-invalid' : errors[field] && blurred[field]}"
            v-on:blur="blurred[field] = true; isValid(field,row[field])"
            v-on:focus="blurred[field] = false; errors[field] = false"
        >

          <option disabled value="">Please select one</option>
          <option
              v-for="(option) in props.choices"
              :key="option.value"
              :value="option.value"
          >
            {{ option.display_name }}
          </option>
        </select>
        <InputSearchSelect v-else-if="props.type==='nested object'" v-model="row[field]" @input="row[field] = $event" :value="row[field]" :info="props" :field="field"/>


        <div class="invalid-tooltip">
          {{ errors[field] }}
        </div>
      </template>
      <template v-else>
        <DisplayNumber v-if="props.type==='integer'" :value="row[field]" :info="props"/>
        <DisplayObject v-else-if="props.type==='nested object'" :value="row[field]" :info="props"/>
        <DisplayString v-else :value="row[field]" :info="props"/>
      </template>
    </td>
    <td class="col-1 text-center col-xs-1">
      <div class="btn-group btn-group-xs" role="group">
        <button :class="'btn btn-xs btn-outline-' + buttonClass" @click="toggle($event)">
          <i :class="'pi pi-' + buttonIcon"></i>
        </button>
        <button class="btn btn-xs btn-outline-danger" @click="removeRow(index)">
          <i class="pi pi-delete-left"></i>
        </button>
      </div>
    </td>
  </tr>
</template>

<script>
import DisplayString from "@/components/GetList/DisplayString.vue";
import DisplayNumber from "@/components/GetList/DisplayNumber.vue";
import DisplayObject from "@/components/GetList/DisplayObject.vue";
import InputSearchSelect from "@/components/GetList/InputSearchSelect.vue";
import {Tooltip} from 'bootstrap'

export default {
  name: 'TableRow',
  components: {
    DisplayString,
    DisplayNumber,
    DisplayObject,
    InputSearchSelect
  },
  props: {
    rowData: Object,
    options: Object,
    tEdit: Boolean,
    url: String,
    index: Number,
  },
  computed: {
    row() {
      return this.rowData
    },
  },
  data() {
    return {
      toggleEdit: this.tEdit,
      blurred: {},
      errors: {},
      buttonIcon: "file-edit",
      buttonClass: "primary"
    };
  },
  mounted() {
    new Tooltip(document.body, {
      selector: "[data-bs-toggle='tooltip']",
    })
  },
  methods: {
    removeRow() {
      if (this.row.id) {
        this.deleteData()
      }
      this.$parent.removeRow(this.index)
    },
    isValid(field, value) {
      if (this.options[field].required && !value) {
        this.errors[field] = 'Required'
        this.blurred[field] = true
        return false
      } else if (this.errors[field]) {
        this.blurred[field] = true
        return false
      }
      return true;
    },
    validate() {
      let valid = true
      for (let field of Object.keys(this.options)) {
        this.blurred[field] = true
        if (!this.isValid(field, this.row[field])) {
          valid = false
        }
      }
      if (valid) {
        this.blurred = {}
        this.errors = {}
      }
      return valid
    },
    async toggle() {
      let proceed = true
      if (this.toggleEdit) {
        this.buttonIcon = "file-edit"
        this.buttonClass = "primary"
        proceed = await this.saveData()
      } else {
        this.buttonIcon = "save"
        this.buttonClass = "info"
      }
      console.log(proceed)
      if (proceed) {
        this.toggleEdit = !this.toggleEdit
      }
      console.log(this.toggleEdit)
    },
    async saveData() {
      if (this.validate()) {
        return fetch(this.url + (this.row.id ? this.row.id + '/' : ''), {
          method: (this.row.id ? 'PUT' : 'POST'),
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify(this.row)
        })
            .then(async response => {
              if ([200, 201].includes(response.status)) {
                let row = await response.json();
                for (let field of Object.keys(row)) {
                  this.row[field] = row[field];
                }
                return true;
              } else if (response.status === 400) {
                this.errors = await response.json();
                for (let field of Object.keys(this.errors)) {
                  this.blurred[field] = true
                }
                return false;
              }
            })
            .catch((err) => {
              console.error(err);
            });
      }
    },
    async deleteData() {
      fetch(this.url + this.row.id + '/', {
        method: 'DELETE',
      })
          .then(async response => {
            return response.status
          })
          .catch((err) => {
            console.error(err);
          });
    },
  },
}
</script>

<style scoped>


.invalid-tooltip {
  top: unset;
}
</style>