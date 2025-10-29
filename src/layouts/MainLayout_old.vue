<template>
  <q-layout view="hHh Lpr lFf">
    <q-header elevated class="bg-primary"> 
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
        />
        <q-toolbar-title>
          Werkblatt Annotator
        </q-toolbar-title>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>

</script>
