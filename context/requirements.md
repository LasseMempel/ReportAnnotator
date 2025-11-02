# Anforderungsdokument (Requirements) für die WaiRKBLAETTER App

---
## 1. Zweck und Nutzung im LLM-gestützten Entwicklungsprozess

**Dieses Dokument ist die Quelle der Wahrheit für die Zukunft der Anwendung.** Es definiert den **gewünschten Zustand** und listet alle geplanten Features, User Stories und zu implementierenden Funktionalitäten auf. Es dient als primäre Arbeitsgrundlage für LLM-Coding-Agenten, um neue Features zu entwickeln oder bestehende zu erweitern.

### Arbeitsanweisungen für LLM-Agenten:

1.  **Status-Tracking**: Alle Anforderungen sind als Markdown-Checklisten formatiert (`- [ ]`).
2.  **Umgang mit unvollständigen Features**: Wenn ein Feature in der Entwicklung ist, aber Fehler aufweist oder unvollständig ist, wird der Status direkt beim entsprechenden Checklist-Eintrag vermerkt.
    - **Beispiel**: `- [ ] Feature X implementieren (Status: In Entwicklung, Bug: Login schlägt bei Sonderzeichen fehl, Fehlende Funktion: Passwort-Reset)`.
3.  **Abschluss eines Features**: Sobald ein Feature **vollständig, fehlerfrei und getestet** implementiert wurde, wird der entsprechende Eintrag **vollständig aus diesem Dokument entfernt**. Die technische Dokumentation des nun implementierten Features wird stattdessen in `docu.md` (lesbare Beschreibung) und `docu.json` (maschinenlesbare Struktur) überführt.
4.  **Fokus**: Dieses Dokument bleibt eine reine, zukunftsorientierte "To-Do"-Liste. Es beschreibt **nicht** den aktuellen Zustand der Anwendung.

---

## 2. Funktionale Anforderungen

### 4.1 Laden und Verarbeiten von SKOS-Vokabularen
- [ ] Import von SKOS-Vokabularen (TTL/RDF) mit `rdflib.js`
- [ ] Extraktion von `skos:prefLabel`, `skos:altLabel`, `skos:definition`, `skos:broader`, `skos:narrower`
- [ ] Darstellung der Hierarchie in einer Baumstruktur
- [ ] Zunächst nur ein Vokabular aktiv
- [ ] Caching von Vokabular-Embeddings in IndexedDB

### 4.2 Sprach- und Textverarbeitung
- [ ] **Automatische Spracherkennung** (Deutsch/Englisch) für Text und Vokabular
- [ ] Wahl des passenden Stemmer je nach Sprache (Deutsch/Englisch)
- [ ] Fallback: Nur Stemming, keine Lemmatisierung (rein JS-basiert)
- [ ] Optionale Nutzung eines **multilingualen Sentence-Transformer-Modells** `Xenova/distiluse-base-multilingual-cased-v1`

### 4.3 Embedding-Berechnung
- [ ] Clientseitige Berechnung mit `transformers.js`
- [ ] Erzeugung von Vektor-Repräsentationen für:
  - Konzepte (Labels + Definitionen + Broader-Relationen)
  - Text-n-Gramme (uni-, bi-, trigramm)
- [ ] Speicherung der Vokabularembeddings für Wiederverwendung

### 4.4 Linking-Algorithmus
- [ ] Kombination aus String- und Embedding-Similarity
- [ ] Konfigurierbare Gewichtung (0–1)
- [ ] Entscheidungslogik:
  - Score > 0.8: akzeptieren
  - 0.6–0.8: unsicher, markieren
  - < 0.6: verwerfen
- [ ] Bei mehreren Treffern: spezifischstes Konzept im Hierarchiebaum bevorzugen
- [ ] Anzeige von Top-n Kandidaten (default: 3)

### 4.5 Benutzerinteraktion
- [ ] Farblich kodierte Hervorhebung im Text (grün = sicher, gelb = unsicher, rot = verworfen)
- [ ] Benutzer können:
  - Vorschläge bestätigen, ablehnen oder korrigieren
  - Neue Begriffe hinzufügen und `skos:broader`-Relation wählen
  - Korrekturen und Annotationen editieren
- [ ] Lokale Speicherung der Korrekturen für Trainingsdatensätze

### 4.6 Vokabularexpansion und Alignment
- [ ] Optionale Einbindung alignter (z. B. englischer) Vokabulare zur Ergänzung fehlender Informationen
- [ ] Embedding-basierte Vorschläge für Synonyme oder fehlende Definitionen
- [ ] Nutzer kann Vorschläge annehmen oder anpassen
- [ ] Speicherung der erweiterten Vokabulare lokal

### 4.7 Datenexport
- [ ] Export der Annotationen und Metadaten als JSON:
  - erkannte Konzepte
  - Ähnlichkeitswerte
  - Kontextinformationen (Satz, Absatz)
  - Nutzerkorrekturen
- [ ] Perspektivisch Export im **NLP Interchange Format (NIF)**

---

## 5. Nicht-funktionale Anforderungen

### 5.1 Performance
- [ ] Berechnung der Embeddings komplett clientseitig (keine Serverlast)
- [ ] Vektorberechnung für bis zu 10.000 Konzepte in <30s
- [ ] Caching von Ergebnissen zur Performance-Steigerung

### 5.2 Datenschutz
- [ ] Keine Serverkommunikation
- [ ] Lokale Persistenz in IndexedDB
- [ ] Volle Offline-Funktionalität

### 5.3 Usability
- [ ] Intuitive Benutzeroberfläche
- [ ] Einstellbare Gewichtung von String-/Embedding-Similarity
- [ ] Visualisierung der Hierarchien und Annotationssicherheit

### 5.4 Erweiterbarkeit
- [ ] Modulare Architektur (Stemming, Embeddings, Linking, Export als unabhängige Module)
- [ ] Vorbereitung für spätere Integration von:
  - POS-Tagging
  - Phrase Chunking
  - NER
  - Relationserkennung

---

## 6. Geplante Erweiterungen

- [ ] **Kontextbasierte Embeddings** (satzweise statt n-Gramme)
- [ ] **POS-Tagging** zur verbesserten Kategorisierung (Substantiv, Verb, Adjektiv)
- [ ] **NER-basierte Heuristiken** zur Vorauswahl
- [ ] **Relationserkennung** zwischen Konzepten im Satzkontext
- [ ] **Human-in-the-loop-Annotation**, sobald ausreichend Daten vorhanden sind
- [ ] **Semantische Suche** im Vokabular (Subgraph-basierte Auswahl)

---

## 7. Forschungsspezifische Softwareanforderungen (RSE)

### 7.1 Testing
- [ ] Unit-Tests für Parsing, Matching, Embedding und Export
- [ ] Integrationstests für Annotation-Workflow
- [ ] Beispiel-Testdatensätze zur Reproduzierbarkeit

### 7.2 CI/CD
- [ ] Versionierung mit Git / GitHub
- [ ] CI mit GitHub Actions:
  - automatisierte Tests
  - Linting (ESLint)
- [ ] Deployment via GitHub Pages / Netlify
- [ ] Semantische Versionierung (Semantic Release)

### 7.3 Dokumentation & FAIRness
- [ ] Reproduzierbarkeit (Versionen der Modelle fixiert)
- [ ] Maschinenlesbare Metadaten (`CITATION.cff`, `README`, `LICENSE`)
- [ ] Nutzer- und Entwicklerdokumentation
- [ ] Exportfunktionen für Daten FAIR-kompatibel

---

## 8. Technologiestack

| Komponente | Technologie |
|-------------|--------------|
| Frontend | Quasar (Vue 3, JavaScript) |
| Vokabular-Parsing | rdflib.js |
| Embeddings | transformers.js + Xenova/distiluse-base-multilingual-cased-v1 |
| String Matching | eigene Implementierung (z. B. Jaro-Winkler, Cosine) |
| Speicherung | IndexedDB |
| Export | JSON, perspektivisch NIF |
| Tests | Vitest / Jest |
| CI/CD | GitHub Actions + Netlify |

---

## 9. Parameterübersicht

| Parameter | Standardwert | Beschreibung |
|------------|---------------|---------------|
| Gewichtung String/Embedding | 0.5 | Balance zwischen beiden Ähnlichkeiten |
| Akzeptanzschwelle | 0.8 | Automatische Verlinkung |
| Unsicherheitsschwelle | 0.6 | Flag für unsichere Treffer |
| Max. Kandidaten | 3 | Anzahl der Vorschläge pro Treffer |
| N-Gramm-Bereich | 1–3 | Konfigurierbare Fenstergröße |

---

## 10. Offene Forschungs- und Designfragen
- Bewertung der Linkingqualität (Precision, Recall, F1)
- Optimale Kombination aus Labels, Definitionen, Relationen für Konzeptvektoren
- Gewichtung hierarchischer Beziehungen bei Konzeptwahl
- UI-Design für effiziente Nutzerkorrekturen
- Nutzung alignter Vokabulare (z. B. AAT, Wikidata) zur Erweiterung

---

## 11. VERPFLICHTENDER PROMPT FÜR LLM-AGENTEN

**Anweisung:** Nach jeder Code-Änderung, die ein Feature aus diesem Dokument implementiert, musst du die folgenden Schritte ausführen:
1.  **Überprüfe**, ob das Feature vollständig, korrekt und ohne bekannte Fehler funktioniert.
2.  **Entferne** den entsprechenden Checklist-Eintrag aus diesem Dokument (`requirements.md`).
3.  **Aktualisiere** die technische Dokumentation in `docu.md` und die maschinenlesbare Struktur in `docu.json`, um den neuen Code-Stand widerzuspiegeln.
4.  Falls das Feature **nicht vollständig** implementiert wurde oder **Fehler** aufweist, **aktualisiere** den entsprechenden Eintrag hier mit einer klaren Beschreibung des Problems, anstatt ihn zu löschen.

**Ende des Dokuments**
