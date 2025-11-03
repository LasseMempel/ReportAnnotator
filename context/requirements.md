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

# Meta-Prompt: Arbeitskontext für die WaiRKBLAETTER App

---
## Anweisung an den LLM-Agenten

Bevor du mit der Bearbeitung der Aufgabe beginnst, mache dich mit der Struktur der bereitgestellten Kontextdokumente vertraut. Jedes Dokument hat einen spezifischen Zweck. Die strikte Einhaltung dieser Struktur ist entscheidend für den Erfolg des Projekts.

### Übersicht der Kontext-Dokumente:

1.  **`C:\repos\WaiRKBLAETTER\context/project.md` - Das "Warum"**
    -   **Zweck**: Enthält die übergeordnete Vision, die Zielsetzung der Anwendung und wichtiges Domänenwissen (z.B. zu SKOS, Embeddings).
    -   **Nutzung**: Lies dieses Dokument, wenn du das grundlegende Ziel einer Anforderung verstehen musst. Dieses Dokument ändert sich selten.

2.  **`C:\repos\WaiRKBLAETTER\context/requirements.md` - Das "Was als Nächstes"**
    -   **Zweck**: Eine reine To-Do-Liste zukünftiger Features und zu behebender Bugs im Markdown-Checklisten-Format.
    -   **Nutzung**: Deine primäre Quelle für neue Entwicklungsaufgaben. Wenn du ein Feature implementiert hast, entfernst du den entsprechenden Eintrag aus dieser Datei.

3.  **`C:\repos\WaiRKBLAETTER\context/architecture.md` - Das "Wie (High-Level)"**
    -   **Zweck**: Beschreibt die technische Architektur, die Hauptkomponenten und den Datenfluss.
    -   **Nutzung**: Konsultiere dieses Dokument, um sicherzustellen, dass dein Code zur Gesamtarchitektur passt.

4.  **`C:\repos\WaiRKBLAETTER\context\docu.md` - Das "Wie (Low-Level, lesbar)"**
    -   **Zweck**: Detaillierte, für Menschen lesbare Dokumentation des *aktuellen, stabilen* Codes.
    -   **Nutzung**: Deine Referenz, um existierende Funktionen, ihre Parameter und ihre Logik zu verstehen. Du bist verpflichtet, dieses Dokument nach jeder Code-Änderung zu aktualisieren.

**Dein Auftrag:**
Implementiere eine prototypische Funktionalität zur Integration von Embedding similarity in den bestehenden Workflow.

- Python script zum Laden des existierenden und vorgeladenen Vokabulars C:\repos\WaiRKBLAETTER\public\thesaurus\thesaurus.ttl
- Berechnung von Embeddings aus skos:prefLabel, skos:broader, skos:altLabel, skos:definition, skos:scopeNote (Geeignete Einbettung in Text mit passenden kurzen, einwörtigenÜberleitungen auswählen: z.B. "Silber, ein/eine/eines Metall, auch ag, weißlich-graues Metall mit dem chemischen Symbol Ag und der Ordnungszahl 47")
- Berücksichtigen, dass nicht immer alle diese Informationen vorhanden sind. label ist für alle Konzepte Pflicht. Alle nicht skosTopConcepts haben auch skos:broader. 
- Speichern der Embeddings in einem Format und einer Datenstruktur, so dass sie gut über js abrufbar und strukturiert ist

-> Diese Funktionen wurden mit dem Python Script C:\repos\WaiRKBLAETTER\scripts\create_embeddings.py bereits ausgeführt und das JSON generiert. Für das Datenmodell checke das Skript, da das Einlesen des JSOn deinen Kontext sprengen würde

- Funktion zum Vektorisieren von Wörtern im Kontext ihres Satzes
- Einpflegung in den aktuellen Workflow - > Vergleich der string-basierten Treffer Wörter in den Sätzen mit den Embeddings ihrer gelinkten SKOS Konzepte (diese Laden)
- On mouseover Anzeige der Sicherheit der identifizierten Begriffe nach Similarity score > gleich 0,8 grün, zwischen 0,6 und 0,8 gelb, unter 0,6 rot

The thesaurus is really big. Under no circumstances try to read thesaurus.ttl
Instead here are some concepts and the conceptScheme, that show you examples:

@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix vann: <http://purl.org/vocab/vann/> .

<https://www.w3id.org/archlink/terms/conservationthesaurus/A14455> a skos:Concept ;
rdfs:seeAlso "https://www.dow.com/en-us/document-viewer.html?docPath=/content/dam/dcc/documents/884/884-01223-01-paraloid-b-72-solid-grade-thermoplastic-acrylic-resin-tds.pdf" ;
skos:altLabel "Acryloid B72"@de,
"Paraloid B-72"@de ;
skos:broader <https://www.w3id.org/archlink/terms/conservationthesaurus/GFD582> ;
skos:definition "Produktname für ein synthestisches Acrylharz der Firma Rohm und Haas (heute Teil von Dow Chemicals), bestehend aus Ethylmethacrylat und Methylacrylat sowie einem kleinen Anteil Butylmethacrylat. Aufgrund seiner hervorragenden Eigenschaften hinsichtlich Alterungsbeständigkeit, Transparenz und Reversibilität ist Paraloid B72 eines der am häufigsten eingesetzten Materialien in der Konservierung und Restaurierung. In verschiedenen organischen Lösungsmitteln gelöst wird es als Klebstoff, Bindemittel, Festigungsmittel und für Schutzüberzug für unterschiedliche Materialien verwendet."@de ;
skos:inScheme <https://www.w3id.org/archlink/terms/conservationthesaurus> ;
skos:notation "A14455" ;
skos:note "Jane L. Down (2015) The evaluation of selected poly(vinyl acetate) and acrylic adhesives: A final research update, Studies in Conservation, 60:1, 33-54, DOI: 10.1179/2047058414Y.0000000129."@de,
"Susan Buys, Victoria Oakley, The conservation and restoration of ceramics (Great Britain 1998), S. 191/192."@de,
"Velson Horie, Materials for Conservation. Organic consolidants, adhesives and coatings (London 2010), S. 159."@de ;
skos:prefLabel "Paraloid B72"@de .

<https://www.w3id.org/archlink/terms/conservationthesaurus/C8CG15> a skos:Concept ;
skos:altLabel "report"@en ;
skos:definition "Sammelbegriff für Aufzeichnungen gemachter Beobachtungen und Handlungen"@de ;
skos:inScheme <https://www.w3id.org/archlink/terms/conservationthesaurus> ;
skos:narrower <https://www.w3id.org/archlink/terms/conservationthesaurus/A8D3G1>,
<https://www.w3id.org/archlink/terms/conservationthesaurus/D3AF3A>,
<https://www.w3id.org/archlink/terms/conservationthesaurus/G76B7G> ;
skos:notation "C8CG15" ;
skos:prefLabel "Dokumentation"@de,
"documentation"@en ;
skos:topConceptOf <https://www.w3id.org/archlink/terms/conservationthesaurus> .

<https://www.w3id.org/archlink/terms/conservationthesaurus> a skos:ConceptScheme ;
dc:creator "Kristina Fella" ;
dc:description "Der Fachthesaurus umfasst eine Vielzahl von deutschen und englischen Begriffen, die für die Zustandserfassung und die Beschreibung von Konservierungs- und Restaurierungsmaßnahmen archäologischer Kulturgüter relevant sind. ."@de ;
dc:title "Konservierungs- und Restaurierungsfachthesaurus für archäologische Kulturgüter"@de ;
dcterms:contributor "Christian Eckmann",
"Waldemar Muskalla" ;
dcterms:license <https://creativecommons.org/licenses/by/4.0/> ;
dcterms:publisher "Leibniz-Zentrum für Archäologie (LEIZA)" ;
dcterms:rights "CC BY 4.0" ;
dcterms:subject "Archäologie"@de,
"Konservierung"@de,
"Restaurierung"@de ;
vann:preferredNamespaceUri "https://www.w3id.org/archlink/terms/conservationthesaurus/" ;
skos:hasTopConcept <https://www.w3id.org/archlink/terms/conservationthesaurus/A18D95>,
<https://www.w3id.org/archlink/terms/conservationthesaurus/C4BCF8>,
<https://www.w3id.org/archlink/terms/conservationthesaurus/C8CG15>,
<https://www.w3id.org/archlink/terms/conservationthesaurus/CFGDA3>,
<https://www.w3id.org/archlink/terms/conservationthesaurus/DAB4B7> .

---

## 11. VERPFLICHTENDER PROMPT FÜR LLM-AGENTEN

**Anweisung:** Nach jeder Code-Änderung, die ein Feature aus diesem Dokument implementiert, musst du die folgenden Schritte ausführen:
1.  **Überprüfe**, ob das Feature vollständig, korrekt und ohne bekannte Fehler funktioniert.
2.  **Entferne** den entsprechenden Checklist-Eintrag aus diesem Dokument (`requirements.md`).
3.  **Aktualisiere** die technische Dokumentation in `docu.md` und die maschinenlesbare Struktur in `docu.json`, um den neuen Code-Stand widerzuspiegeln.
4.  Falls das Feature **nicht vollständig** implementiert wurde oder **Fehler** aufweist, **aktualisiere** den entsprechenden Eintrag hier mit einer klaren Beschreibung des Problems, anstatt ihn zu löschen.

**Ende des Dokuments**
