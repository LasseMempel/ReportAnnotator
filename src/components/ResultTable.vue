<template>
  <q-card v-if="store.tableResultObject?.length" flat bordered>
    <q-toolbar>
      <div class="text-h6">Konzepte</div>
    </q-toolbar>
    <q-table
      :rows="store.tableResultObject"
      :columns="columns"
      row-key="uri"
      flat
      dense
      wrap-cells
    />
  </q-card>
</template>

<script setup>
import { useTextStore } from '../stores/TextStore'

const store = useTextStore()

const columns = [
  {
    name: 'uri',
    label: 'URI',
    field: 'uri',
    align: 'left',
    sortable: true,
    style: 'max-width: 25%; word-break: break-word'
  },
  {
    name: 'prefLabel',
    label: 'Preferred Label',
    field: 'prefLabel',
    sortable: true,
    style: 'white-space: normal;'
  },
  {
    name: 'altLabel',
    label: 'Alternative Labels',
    field: 'altLabels',
    format: val => Array.isArray(val) ? val.join(', ') : val,
    style: 'white-space: normal;'
  },
  {
    name: 'definition',
    label: 'Definition',
    field: 'definition'
  }
]
</script>
