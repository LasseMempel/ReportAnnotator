<template>
  <q-page class="column items-center q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 1200px; width: 100%">
      <!-- 3 file inputs in a row -->
      <div class="row q-gutter-md">
        <div class="col">
          <ThesaurusInput />
        </div>
        <div class="col">
          <FileInput
            v-model="fileInputRef"
            @file-processed="(text) => handleProcessedFile(text, 'fileInput')"
          />
        </div>
        <div class="col">
          <OcrFileInput
            v-model="ocrFileInputRef"
            @file-processed="(text) => handleProcessedFile(text, 'ocrInput')"
          />
        </div>
      </div>

      <!-- Text input and controls -->
      <q-card flat bordered>
        <q-card-section>
          <q-form @submit.prevent="onSubmit" @reset="onReset" class="q-gutter-md">
            <q-input
              label="Paste Text"
              v-model="localInputText"
              type="textarea"
              filled
              autogrow
            />
            <q-toggle v-model="stemming" label="Stemming" />
            <q-card-actions align="right">
              <q-btn label="Analyze" type="submit" color="accent" />
              <q-btn label="Reset" type="reset" color="accent" flat />
            </q-card-actions>
          </q-form>
        </q-card-section>
      </q-card>

      <!-- Results -->
      <ResultCard />
      <ResultTable />
    </div>
  </q-page>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useTextStore } from '../stores/TextStore'
import { useQuasar } from 'quasar'

import FileInput from '../components/FileInput.vue'
import OcrFileInput from '../components/OcrFileInput.vue'
import ThesaurusInput from 'src/components/ThesaurusInput.vue'
import ResultCard from 'src/components/ResultCard.vue'
import ResultTable from 'src/components/ResultTable.vue'

import { calculateResult } from '../utils/annotationResult.js'

const $q = useQuasar()
const store = useTextStore()

const localInputText = computed({
  get: () => store.inputText,
  set: (value) => store.setInputText(value)
})

const fileInputRef = ref(null)
const ocrFileInputRef = ref(null)
const stemming = ref(false)

const handleProcessedFile = (text, source) => {
  store.setInputText(text.replace(/\n\s*\n/g, '\n\n'))
  
  if (source === 'fileInput' && ocrFileInputRef.value) {
    ocrFileInputRef.value = null
  } else if (source === 'ocrInput' && fileInputRef.value) {
    fileInputRef.value = null
  }
}

const onSubmit = async () => {
  if (!store.inputText.trim()) {
    $q.notify('No text to analyze')
    return
  }
  const result = calculateResult(store.inputText, store.labelsMap, store.stemmedLabelsMap, store.conceptsMap, stemming.value)
  const tableResultObject = result[1]
  const annotationResultObject = result[0]
  store.setTableResultObject(tableResultObject)
  store.setAnnotationResultObject(annotationResultObject)
}

const onReset = () => {
  store.resetText()
  
  if (fileInputRef.value) fileInputRef.value = null
  if (ocrFileInputRef.value) ocrFileInputRef.value = null
}
</script>
