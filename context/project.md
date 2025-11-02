# Projektdokumentation: WaiRKBLAETTER App

---
## 1. Zweck und Nutzung im LLM-gestützten Entwicklungsprozess

**Dieses Dokument ist die zentrale Quelle der Wahrheit für das "Warum" des Projekts.** Es enthält die übergeordnete Vision, die Zielsetzung der Anwendung und grundlegendes Domänenwissen. Es dient als konzeptionelle Grundlage für alle Entwicklungsaktivitäten.

### Arbeitsanweisungen für LLM-Agenten:

1.  **Als Erstes lesen**: Konsultiere dieses Dokument, um den allgemeinen Kontext und das Ziel einer neuen Anforderung zu verstehen.
2.  **Selten ändern**: Dieses Dokument wird nur bei grundlegenden Änderungen an der Projektvision oder der Zielgruppe aktualisiert.

---

## 2. Projektvision und Zielsetzung

Diese Webanwendung soll es Nutzern ermöglichen, kontrollierte Vokabulare im **SKOS-Format** zu laden, sie in Texten anzuwenden und dadurch Konzepte zu identifizieren und zu verlinken. Neben **String-basierten Matching-Algorithmen** sollen **Embeddings** eingesetzt werden, um die Treffergenauigkeit zu verbessern. Dabei soll die Anwendung **rein clientbasiert** funktionieren, ohne Serverkommunikation, um maximalen Datenschutz und Offline-Fähigkeit zu gewährleisten.

---

## 3. Systemkontext und Zielgruppe

-   **Art der Anwendung:** Rein clientbasierte WebApp (Vue 3 / Quasar, JavaScript)
-   **Daten:** SKOS Vokabulare (.ttl, .rdf), Textdokumente, JSON Exporte
-   **Zielgruppe:** Forschende im Bereich der Digital Humanities, Konservierung-Restaurierung, semantische Modellierung und alle, die Texte mit standardisierten Vokabularen erschließen möchten.
-   **Datenschutz:** Keine externe Datenübertragung, alle Daten verbleiben im Browser des Nutzers. Lokale Speicherung erfolgt via IndexedDB.
-   **Kompatibilität:** Die Anwendung ist als Progressive Web App (PWA) konzipiert und funktioniert vollständig offline.

---

## 4. Wichtiges Domänenwissen

### 4.1 SKOS (Simple Knowledge Organization System)

-   **Was es ist**: SKOS ist ein W3C-Standard zur Darstellung von kontrollierten Vokabularen wie Thesauri, Klassifikationssystemen oder Taxonomien.
-   **Kernkonzepte**:
    -   `skos:Concept`: Eine Idee oder ein Gedanke (z.B. "Email", "Punze").
    -   `skos:prefLabel`: Das bevorzugte Label für ein Konzept (z.B. "Emaille").
    -   `skos:altLabel`: Ein alternatives Label oder Synonym (z.B. "Schmelzglas").
    -   `skos:definition`: Eine Beschreibung des Konzepts.
    -   `skos:broader` / `skos:narrower`: Definiert hierarchische Beziehungen (Ober- und Unterbegriffe).
-   **Relevanz für das Projekt**: Die Anwendung parst SKOS-Dateien, um diese strukturierten Informationen für das Text-Linking zu nutzen.

### 4.2 Semantische Ähnlichkeit mit Embeddings

-   **Was es ist**: Text-Embeddings sind Vektor-Repräsentationen von Wörtern oder Sätzen in einem hochdimensionalen Raum. Die Distanz und der Winkel zwischen den Vektoren repräsentieren die semantische Ähnlichkeit der Texte.
-   **Wie es funktioniert**: Modelle wie `distiluse-base-multilingual-cased-v1` (ein Sentence-Transformer-Modell) werden trainiert, um Texte mit ähnlicher Bedeutung nahe beieinander im Vektorraum zu platzieren.
-   **Relevanz für das Projekt**: Anstatt nur auf exakte Wortübereinstimmungen zu prüfen, kann die Anwendung die semantische Ähnlichkeit zwischen einem Textsegment und den Konzeptdefinitionen aus dem SKOS-Vokabular berechnen. Dies ermöglicht die Identifizierung von Konzepten, auch wenn andere Wörter verwendet werden (z.B. "Schmelzüberzug" könnte als ähnlich zu "Emaille" erkannt werden).

**Ende des Dokuments**
