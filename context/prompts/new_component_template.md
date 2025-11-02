# Prompt-Vorlage: Erstellung einer neuen Vue-Komponente

---
## Anweisung an den LLM-Agenten

Du bist ein erfahrener Vue.js 3 Entwickler, der mit der Composition API und dem Quasar Framework vertraut ist. Deine Aufgabe ist es, eine neue, wiederverwendbare Vue-Komponente zu erstellen, die den höchsten Qualitätsstandards und den Konventionen dieses Projekts entspricht.

---
## 1. Kontext und Ziel der Komponente

**Beschreibung:**
`[Hier eine klare und prägnante Beschreibung einfügen, was die Komponente tun soll. Welches Problem löst sie? Was ist ihr primärer Zweck?]`

**Beispiel:**
`"Erstelle eine Komponente, die es dem Benutzer ermöglicht, eine Textdatei per Drag-and-Drop oder über einen Dateiauswahldialog hochzuladen. Die Komponente soll den Inhalt der Datei als String ausgeben."`

---
## 2. Technische Spezifikationen

**Props (Eingabeparameter):**
`[Liste hier alle Props auf, die die Komponente akzeptieren soll. Gib für jede Prop den Namen, den erwarteten Typ (z.B. String, Number, Array, Object), ob sie erforderlich ist (required) und einen Standardwert (default) an.]`

**Beispiel:**
```javascript
props: {
  allowedFileTypes: {
    type: Array,
    required: false,
    default: () => ['.txt', '.ttl']
  },
  maxFileSizeMB: {
    type: Number,
    required: false,
    default: 5
  }
}
```

**Emits (Ausgabe-Events):**
`[Liste hier alle Events auf, die die Komponente auslösen kann. Gib den Namen des Events und die Daten an, die mit dem Event übergeben werden (Payload).]`

**Beispiel:**
```javascript
emits: ['file-loaded', 'error']

// Event 'file-loaded' Payload: { fileName: String, fileContent: String }
// Event 'error' Payload: { message: String }
```

**Slots:**
`[Beschreibe alle Slots, die die Komponente zur Verfügung stellt, damit übergeordnete Komponenten eigenen Inhalt einfügen können.]`

**Beispiel:**
`"Die Komponente soll einen default-Slot haben, um einen benutzerdefinierten Text oder ein Icon im Drop-Bereich anzuzeigen."`

---
## 3. Anforderungen an die Implementierung

-   **Frameworks**: Nutze Vue 3 mit der `<script setup>`-Syntax (Composition API). Verwende Quasar-Komponenten (z.B. `q-btn`, `q-icon`, `q-uploader`) für das UI, um ein konsistentes Design zu gewährleisten.
-   **Reaktivität**: Verwende `ref` oder `reactive` für den internen Zustand.
-   **Fehlerbehandlung**: Implementiere eine robuste Fehlerbehandlung. Gib klare Fehlermeldungen über das `error`-Event aus (z.B. bei falschem Dateityp oder zu großer Datei).
-   **Code-Stil**: Halte dich an die im Projekt etablierten Code-Stile (ESLint-Regeln). Der Code muss sauber, lesbar und gut kommentiert sein.
-   **Dateiname**: Die Komponente soll in `src/components/` unter dem Namen `[ComponentName].vue` gespeichert werden.

---
## 4. Beispiel für die Verwendung (optional)

`[Füge hier ein kurzes Code-Snippet ein, das zeigt, wie die neue Komponente in einer übergeordneten Komponente verwendet werden würde.]`

**Beispiel:**
```vue
<template>
  <NewFileInput @file-loaded="handleFile" @error="handleError" />
</template>

<script setup>
function handleFile(payload) {
  console.log('Datei geladen:', payload.fileName);
}
function handleError(error) {
  console.error('Fehler:', error.message);
}
</script>
