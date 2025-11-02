# Technische Dokumentation der WaiRKBLAETTER App

---
## 1. Zweck und Nutzung im LLM-gestützten Entwicklungsprozess

**Dieses Dokument ist die Quelle der Wahrheit für die Gegenwart.** Es beschreibt den **aktuellen, stabilen und funktionierenden Zustand** des Programmcodes. Es dient als detaillierte technische Referenz für LLM-Coding-Agenten, um die bestehende Implementierung zu verstehen, darauf aufzubauen und sie zu warten.

### Arbeitsanweisungen für LLM-Agenten:

1.  **Als Referenz nutzen**: Konsultiere dieses Dokument, um die Funktionsweise, Parameter und Rückgabewerte existierender Funktionen und Komponenten zu verstehen.
2.  **Dokumentation aktuell halten**: Nach jeder erfolgreichen Implementierung eines neuen Features oder einer Änderung am Code **muss dieses Dokument aktualisiert werden**, um den neuen Stand korrekt widerzuspiegeln. Die Informationen über das implementierte Feature werden aus `requirements.md` entfernt und hier in technischer Form hinzugefügt.
3.  **Fokus**: Dieses Dokument beschreibt ausschließlich den **tatsächlich implementierten Code**. Geplante, aber noch nicht umgesetzte Features gehören in die `requirements.md`.

---

## 2. Dokumentation der Quellcode-Module

### 3.1 `src/utils/` - Kernlogik und Algorithmen

Das `utils`-Verzeichnis enthält die zentrale Geschäftslogik der Anwendung in Form von unabhängigen JavaScript-Modulen.

#### **`nlp.js` - Natural Language Processing**
Dieses Modul stellt grundlegende NLP-Funktionen zur Verfügung.

-   **`tokenizeSentences(text)`**
    -   **Beschreibung**: Zerlegt einen Eingabetext in einzelne Sätze. Nutzt die browser-native `Intl.Segmenter` API für die deutsche Sprache.
    -   **Parameter**:
        -   `text` (String): Der zu segmentierende Text.
    -   **Output**: `Array<String>` - Ein Array von Sätzen.

-   **`tokenizeWords(text)`**
    -   **Beschreibung**: Zerlegt einen Eingabetext in einzelne Wörter. Nutzt ebenfalls `Intl.Segmenter`.
    -   **Parameter**:
        -   `text` (String): Der zu segmentierende Text.
    -   **Output**: `Array<String>` - Ein Array von Wörtern.

-   **`getNGrams(input, n)`**
    -   **Beschreibung**: Erzeugt n-Gramme aus einem Array von Wörtern. Basiert auf der `n-gram`-Bibliothek.
    -   **Parameter**:
        -   `input` (Array<String>): Ein Array von Tokens (Wörtern).
        -   `n` (Integer): Die Größe der n-Gramme (z.B. 2 für Bigramme).
    -   **Output**: `Array<Array<String>>` - Ein Array, das die n-Gramme enthält.

-   **`lowerCase(input)` / `upperCase(input)`**
    -   **Beschreibung**: Konvertiert einen String in Klein- bzw. Großbuchstaben.
    -   **Parameter**: `input` (String).
    -   **Output**: `String`.

#### **`rdf.js` - RDF- und SKOS-Verarbeitung**
Dieses Modul ist für das Parsen und Verarbeiten von Vokabularen im Turtle/RDF-Format zuständig.

-   **`processTurtleContent(fileContent)`**
    -   **Beschreibung**: Parst einen Turtle-String (`.ttl`), extrahiert alle `skos:Concept`-Instanzen und deren `skos:prefLabel`, `skos:altLabel` (nur deutsch) und `skos:definition`. Strukturelle Konzepte (deren Label mit `[` beginnt) werden ignoriert.
    -   **Algorithmus**:
        1.  Initialisiert einen `rdflib.js`-Store.
        2.  Parst den `fileContent`.
        3.  Sucht alle Tripel mit `rdf:type` `skos:Concept`.
        4.  Iteriert durch die gefundenen Konzepte und extrahiert die zugehörigen Labels und Definitionen.
        5.  Erstellt zwei Maps: `conceptsMap` (URI -> {prefLabel, altLabel, definition}) und `labelsMap` (Label -> [URIs]).
    -   **Parameter**:
        -   `fileContent` (String): Der Inhalt der `.ttl`-Datei als String.
    -   **Output**: `Array` - Ein Array mit zwei Elementen: `[conceptsMap, labelsMap]`.

#### **`cistem.js` - Deutscher Stemmer**
Implementiert den CISTEM-Algorithmus zur Reduktion deutscher Wörter auf ihren Wortstamm.

-   **`stem(word, case_insensitive = false)`**
    -   **Beschreibung**: Führt das Stemming für ein einzelnes deutsches Wort durch.
    -   **Parameter**:
        -   `word` (String): Das zu stemmende Wort.
        -   `case_insensitive` (Boolean): Ob die Groß-/Kleinschreibung ignoriert werden soll.
    -   **Output**: `String` - Der gestemmte Wortstamm.

#### **`helper.js` - Hilfsfunktionen**
Enthält unterstützende Funktionen, die von anderen Teilen der Anwendung genutzt werden.

-   **`generateStemmedLabelsMap(labelsMap)`**
    -   **Beschreibung**: Erstellt aus einer gegebenen `labelsMap` eine zusätzliche Map, in der die Schlüssel (Labels) gestemmt sind. Dies dient dem späteren Abgleich von gestemmten Wörtern aus dem Input-Text.
    -   **Algorithmus**:
        1.  Iteriert durch die `labelsMap`.
        2.  Verarbeitet nur Ein-Wort-Begriffe, die nicht komplett in Großbuchstaben geschrieben sind.
        3.  Stemmt den Begriff mit der `stem()`-Funktion aus `cistem.js`.
        4.  Fügt den gestemmten Begriff und die zugehörigen URIs zur neuen `stemmedLabelsMap` hinzu.
    -   **Parameter**:
        -   `labelsMap` (Object): Eine Map, bei der die Schlüssel Labels und die Werte Arrays von Concept-URIs sind.
    -   **Output**: `Object` - Die `stemmedLabelsMap`.

### 3.2 `src/stores/` - Globales State Management

Das `stores`-Verzeichnis enthält die Pinia-Stores zur zentralen Verwaltung des Anwendungszustands.

#### **`TextStore.js`**
Der `TextStore` ist der zentrale Speicher für alle Daten, die für die Textanalyse und -annotation relevant sind.

-   **State Properties**:
    -   `inputText` (ref<String>): Der vom Nutzer eingegebene Text.
    -   `conceptsMap` (ref<Object>): Die vom `rdf.js`-Modul erzeugte Map der SKOS-Konzepte.
    -   `labelsMap` (ref<Object>): Die Map der Labels zu Concept-URIs.
    -   `stemmedLabelsMap` (ref<Object>): Die Map der gestemmten Labels.
    -   `annotationResultObject` (ref<Object>): Das Ergebnisobjekt der Annotations-Pipeline.
    -   `tableResultObject` (ref<Array>): Die für die Ergebnistabelle formatierte Version der Annotationen.

-   **Actions (Methoden)**:
    -   `setInputText(text)`: Setzt den `inputText`.
    -   `setConceptsMap(object)`: Setzt die `conceptsMap`.
    -   `setLabelsMap(object)`: Setzt die `labelsMap` und triggert automatisch die Erstellung der `stemmedLabelsMap`.
    -   `setStemmedLabelsMap(object)`: Setzt die `stemmedLabelsMap`.
    -   `setAnnotationResultObject(object)`: Setzt das `annotationResultObject`.
    -   `setTableResultObject(object)`: Setzt das `tableResultObject`.
    -   `resetText()`: Setzt alle State Properties auf ihre initialen Werte zurück.

---

## 4. VERPFLICHTENDER PROMPT FÜR LLM-AGENTEN

**Anweisung:** Nach jeder Code-Änderung, die eine Funktion hinzufügt, entfernt oder deren Signatur (Parameter, Rückgabewert) ändert, **musst du dieses Dokument aktualisieren**. Stelle sicher, dass die Beschreibung hier exakt den implementierten Code widerspiegelt. Neue Module oder wesentliche Änderungen in der Logik müssen ebenfalls hier dokumentiert werden.

**Ende des Dokuments**
