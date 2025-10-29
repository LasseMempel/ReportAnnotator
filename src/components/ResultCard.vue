<template>
  <q-card v-if="store.annotationResultObject?.length" flat bordered>
    <q-card-section class="text-h6">
      Annotation
    </q-card-section>
    <q-card-section>
      <div 
        v-for="(sentence, sIndex) in store.annotationResultObject" 
        :key="sIndex" 
        class="q-mb-sm"
      >
        <span 
          v-for="(segment, segIndex) in sentence.segments" 
          :key="`${sIndex}-${segIndex}`"
          :class="{ 'text-primary': segment.highlighted }"
        >
          {{ segment.text }}
        </span>
      </div>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { useTextStore } from '../stores/TextStore'

const store = useTextStore()
</script>
