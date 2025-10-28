<template>
    <div class="q-pa-md">
      <q-table
        v-if ="store.tableResultObject && store.tableResultObject.length > 0"
        title="Konzepte"
        :rows="store.tableResultObject"
        :columns="columns"
        row-key="uri"
        wrap-cells
        dense
        class="full-width"
      />
    </div>
</template>

<script setup>

import { useTextStore } from '../stores/TextStore'
const store = useTextStore()

const columns = [
  {
    name: 'uri',
    required: true,
    label: 'URI',
    align: 'left',
    field: row => row.uri,
    format: val => `${val}`,
    sortable: true,
    style: 'max-width: 25%; word-break: break-word'
  },
  { 
    name: 'prefLabel', 
    label: 'Preferred Label', 
    field: 'prefLabel', 
    sortable: true 
  },
  { 
    name: 'altLabel', 
    label: 'Alternative Labels', 
    field: 'altLabels', 
    format: val => Array.isArray(val) ? val.join(', ') : val
  },
  { 
    name: 'definition', 
    label: 'Definition', 
    field: 'definition' 
  }
]

</script>
