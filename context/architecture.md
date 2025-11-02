# Architekturdokument für die WaiRKBLAETTER App

---
## 1. Zweck und Nutzung im LLM-gestützten Entwicklungsprozess

**Dieses Dokument beschreibt die High-Level-Architektur und die grundlegenden Design-Entscheidungen der Anwendung.** Es dient als konzeptioneller Leitfaden für LLM-Coding-Agenten, um sicherzustellen, dass neue Features und Änderungen konsistent mit der bestehenden Struktur und den Kernprinzipien der Software entwickelt werden.

### Arbeitsanweisungen für LLM-Agenten:

1.  **Vor jeder größeren Code-Änderung konsultieren**: Lies dieses Dokument, um das Zusammenspiel der Komponenten und den beabsichtigten Datenfluss zu verstehen.
2.  **Konsistenz wahren**: Stelle sicher, dass dein Code den hier beschriebenen Mustern folgt (z.B. Trennung von UI, State-Management und Business-Logik).
3.  **Architektur-Änderungen dokumentieren**: Wenn eine Entwicklungsaufgabe eine Änderung an der hier beschriebenen Kernarchitektur erfordert, muss dieses Dokument entsprechend aktualisiert werden. Solche Änderungen sollten explizit im Commit vermerkt werden.

---

## 2. Architektur-Überblick

### 2.1 Kernprinzipien

-   **Rein Client-basiert**: Die gesamte Anwendung läuft ausschließlich im Browser des Nutzers. Es gibt keine Server-Komponente. Dies garantiert maximalen Datenschutz und Offline-Fähigkeit.
-   **Modularität**: Die Anwendungslogik ist in klar getrennte, wiederverwendbare Module (Vue Components, Pinia Stores, Utility-Funktionen) aufgeteilt.
-   **Reaktivität**: Der Zustand der Anwendung wird zentral verwaltet (Pinia), und die UI reagiert automatisch auf Zustandsänderungen.
-   **Zustandslosigkeit der Logik**: Die Kernalgorithmen (NLP, RDF-Parsing etc.) sind in `utils`-Funktionen gekapselt, die in der Regel zustandslos sind (Input rein, Output raus), was ihre Testbarkeit und Wiederverwendbarkeit erhöht.

### 2.2 Technologiestack

-   **Frontend-Framework**: Vue 3 (Composition API) mit dem Quasar Framework für UI-Komponenten.
-   **State Management**: Pinia für das zentrale, reaktive Zustandsmanagement.
-   **Routing**: Vue Router für die Navigation zwischen den Anwendungsseiten.
-   **RDF-Verarbeitung**: `rdflib.js` zum Parsen von SKOS-Vokabularen.
-   **Machine Learning**: `transformers.js` für die clientseitige Berechnung von Text-Embeddings.
-   **Lokale Speicherung**: IndexedDB zur Persistenz von Vokabular-Daten und Annotationen.

---

## 3. Struktur der Codebasis

Die Codebasis ist nach den Konventionen eines typischen Vue/Quasar-Projekts organisiert:

-   **`src/`**: Hauptverzeichnis des Quellcodes.
    -   **`components/`**: Enthält wiederverwendbare Vue-Komponenten, die die Benutzeroberfläche zusammensetzen (z.B. `ResultTable.vue`, `ThesaurusInput.vue`).
    -   **`pages/`**: Enthält die Top-Level-Vue-Komponenten, die ganze Seiten repräsentieren (z.B. `IndexPage.vue`).
    -   **`layouts/`**: Definiert die übergeordneten Seitenlayouts (z.B. mit Header, Footer, Navigation).
    -   **`stores/`**: Beinhaltet die Pinia-Stores für das globale State Management. Der `TextStore.js` verwaltet beispielsweise den zu analysierenden Text und die dazugehörigen Annotationen.
    -   **`router/`**: Konfiguriert das clientseitige Routing der Anwendung.
    -   **`boot/`**: Enthält Initialisierungs-Skripte, die beim Start der App ausgeführt werden (z.B. für Axios).
    -   **`utils/`**: Enthält die Kernlogik der Anwendung in Form von reinen JavaScript-Modulen. Hier finden sich die Algorithmen für NLP (`nlp.js`), RDF-Verarbeitung (`rdf.js`), Stemming (`cistem.js`) und andere Hilfsfunktionen (`helper.js`). Dies ist das "Gehirn" der Anwendung.
    -   **`assets/`**, **`css/`**: Statische Ressourcen wie Bilder und globale Stylesheets.

---

## 4. Datenfluss (High-Level)

1.  **Initialisierung**: Die App startet, Layouts und die `IndexPage` werden geladen.
2.  **Vokabular laden**: Der Nutzer wählt eine SKOS-Datei aus.
    -   Die `FileInput`-Komponente übergibt die Datei an eine Funktion im `rdf.js`-Utility.
    -   `rdf.js` parst die Datei und extrahiert die SKOS-Konzepte.
    -   Die extrahierten Daten werden im zuständigen Pinia-Store gespeichert.
3.  **Text eingeben**: Der Nutzer gibt einen Text in die Anwendung ein.
    -   Der Text wird im `TextStore` gespeichert.
4.  **Analyse & Linking**: Der Linking-Prozess wird gestartet.
    -   Die Kernlogik in `nlp.js` wird aufgerufen.
    -   `nlp.js` zerlegt den Text (z.B. in n-Gramme).
    -   Für die Textsegmente und die SKOS-Konzepte werden mithilfe von `transformers.js` Embeddings berechnet.
    -   Ein Matching-Algorithmus (Kombination aus String-Ähnlichkeit und Vektor-Ähnlichkeit) identifiziert potenzielle Links.
    -   Die Ergebnisse (Annotationen) werden im `TextStore` gespeichert.
5.  **Visualisierung & Interaktion**:
    -   Die `IndexPage` und ihre Kindkomponenten (`ResultTable.vue` etc.) reagieren auf die Änderungen im Store und zeigen die annotierten Ergebnisse an.
    -   Der Nutzer kann Vorschläge bestätigen oder ablehnen, was wiederum den Zustand im Store aktualisiert.
6.  **Export**: Der Nutzer exportiert die Annotationen.
    -   Eine Funktion liest den finalen Zustand aus dem Store und generiert eine JSON-Datei.

---

## 5. VERPFLICHTENDER PROMPT FÜR LLM-AGENTEN

**Anweisung:** Bevor du eine grundlegende Änderung an der Anwendungsstruktur vornimmst (z.B. ein neues State-Management-Pattern einführst, die Ordnerstruktur änderst oder den Datenfluss maßgeblich veränderst), **überprüfe und aktualisiere dieses Dokument**, um die neuen Gegebenheiten widerzuspiegeln. Begründe die Änderung im Commit.

**Ende des Dokuments**
