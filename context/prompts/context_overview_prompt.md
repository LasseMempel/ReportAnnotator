# Meta-Prompt: Arbeitskontext für die WaiRKBLAETTER App

---
## Anweisung an den LLM-Agenten

Bevor du mit der Bearbeitung der Aufgabe beginnst, mache dich mit der Struktur der bereitgestellten Kontextdokumente vertraut. Jedes Dokument hat einen spezifischen Zweck. Die strikte Einhaltung dieser Struktur ist entscheidend für den Erfolg des Projekts.

### Übersicht der Kontext-Dokumente:

1.  **`context/project.md` - Das "Warum"**
    -   **Zweck**: Enthält die übergeordnete Vision, die Zielsetzung der Anwendung und wichtiges Domänenwissen (z.B. zu SKOS, Embeddings).
    -   **Nutzung**: Lies dieses Dokument, wenn du das grundlegende Ziel einer Anforderung verstehen musst. Dieses Dokument ändert sich selten.

2.  **`context/requirements.md` - Das "Was als Nächstes"**
    -   **Zweck**: Eine reine To-Do-Liste zukünftiger Features und zu behebender Bugs im Markdown-Checklisten-Format.
    -   **Nutzung**: Deine primäre Quelle für neue Entwicklungsaufgaben. Wenn du ein Feature implementiert hast, entfernst du den entsprechenden Eintrag aus dieser Datei.

3.  **`context/architecture.md` - Das "Wie (High-Level)"**
    -   **Zweck**: Beschreibt die technische Architektur, die Hauptkomponenten und den Datenfluss.
    -   **Nutzung**: Konsultiere dieses Dokument, um sicherzustellen, dass dein Code zur Gesamtarchitektur passt.

4.  **`context/docu.md` - Das "Wie (Low-Level, lesbar)"**
    -   **Zweck**: Detaillierte, für Menschen lesbare Dokumentation des *aktuellen, stabilen* Codes.
    -   **Nutzung**: Deine Referenz, um existierende Funktionen, ihre Parameter und ihre Logik zu verstehen. Du bist verpflichtet, dieses Dokument nach jeder Code-Änderung zu aktualisieren.

5.  **`context/docu.json` - Das "Wie (Low-Level, maschinenlesbar)"**
    -   **Zweck**: Strukturierte JSON-Repräsentation des *aktuellen, stabilen* Codes.
    -   **Nutzung**: Kann direkt von dir geparst werden, um eine schnelle, fehlerfreie Analyse der Code-Struktur (Module, Funktionen, State) durchzuführen. Muss ebenfalls nach jeder Code-Änderung aktualisiert werden.

**Dein Auftrag:**
`[HIER DEN EIGENTLICHEN AUFTRAG EINFÜGEN]`

**Beispiel:**
`"Implementiere das Feature 'Datenexport als NIF' aus der requirements.md. Stelle sicher, dass die Implementierung der in architecture.md beschriebenen modularen Struktur folgt und aktualisiere nach Abschluss docu.md und docu.json."`
