<template>
  <div class="q-pa-md"> <!-- ✅ Add this wrapper -->
    <q-card v-if="store.annotationResultObject && store.annotationResultObject.length > 0">
      <q-card-section class="q-py-xs q-px-sm">
        <h6 class="q-my-none">Annotation</h6>
      </q-card-section>
      <q-card-section class="q-pt-xs q-pb-sm q-px-sm">
        <div v-for="(sentence, sIndex) in store.annotationResultObject" 
             :key="sIndex" 
             class="sentence q-mb-sm">
          <span v-for="(segment, segIndex) in sentence.segments" 
                :key="`${sIndex}-${segIndex}`"
                :class="{ 'highlighted-text': segment.highlighted }">
            {{ segment.text }}
          </span>
        </div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script setup>
import { useTextStore } from '../stores/TextStore'

const store = useTextStore()
</script>

<style scoped>
.sentence {
  line-height: 1.6;
}

.highlighted-text {
  color: blue;
  font-weight: 500;
}
</style>
