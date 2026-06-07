# PROJECT_OVERVIEW

## 1. Projektziel

Das Projekt ist ein Python-basierter Schildgenerator mit grafischer Benutzeroberfläche (Tkinter).

Ziel ist die Erstellung professioneller:

* Lagerplatzschilder
* QR-Code-Schilder
* Textschilder
* Sicherheitsschilder
* Parkplatzschilder
* Bereichsschilder

Das Projekt soll langfristig modular, wartbar und erweiterbar aufgebaut werden.

---

## 2. Aktuelle Projektphase

### Phase 1: Architektur und Modularisierung

Aktuelle Priorität:

* Projektstruktur verbessern
* Verantwortlichkeiten trennen
* Module auslagern
* main.py verkleinern
* Abhängigkeiten reduzieren
* Wartbarkeit erhöhen
* GitHub-Struktur optimieren

Wichtig:

Neue Funktionen haben aktuell keine Priorität.

Die Grundarchitektur soll zuerst stabil und sauber aufgebaut werden.

---

## 3. Bereits vorhandene Funktionen

* QR-Code-Erzeugung
* PDF-Erzeugung
* 4-Zeilen Layout
* 5-Zeilen Layout
* Firmenlogo
* Rahmen
* Batch-Verarbeitung
* GUI mit Tabs
* Handbuch-Button
* Kontakt-/Support-Button
* Textschildgenerator
* Safe-Area-System
* Automatische Schriftgrößenanpassung
* Automatischer Textumbruch
* Mehrzeilige Zentrierung

---

## 4. Bereits umgesetzte Modularisierung

Ausgelagerte Komponenten:

* validators.py
* layouts.py
* paths.py

Neue Funktionen:

* generate_text_sign_pdf()

---

## 5. Wichtige Dateien

Aktuell:

* main.py
* app.py
* src/pdf/generator.py
* validators.py
* layouts.py
* paths.py

---

## 6. Verwendete Bibliotheken

* Tkinter
* ReportLab
* Pillow
* qrcode
* openpyxl

---

## 7. Gelöste Fehler

* Logo-Pfad korrigiert
* Importfehler behoben
* font_size Fehler behoben
* Safe-Area Berechnung korrigiert
* Button-Validierung ausgelagert

---

## 8. Angestrebte Zielstruktur

```text
src/
├── gui/
├── pdf/
├── services/
├── config/
├── utils/
├── assets/
├── docs/
└── tests/
```

Die Zielstruktur darf angepasst werden, wenn technische Gründe dies sinnvoll erscheinen lassen.

---

## 9. Aktuelle Prioritäten

### Priorität 1

Architektur und Modularisierung

* Verantwortlichkeiten trennen
* Module auslagern
* main.py entschlacken
* Importstrukturen bereinigen

### Priorität 2

Stabilisierung

* Fehlerbehandlung
* Codebereinigung
* Logging
* Testbarkeit

### Priorität 3

Dokumentation

* README
* PROJECT_OVERVIEW
* CHANGELOG

### Priorität 4

Funktionsausbau

Erst nach Abschluss der Modularisierung:

* Vorschaufenster
* Ausrichtungen
* Schriftarten
* A3/A4/A5 Verwaltung
* weitere Schildtypen

---

## 10. Entwicklungsregeln

Bei jeder Änderung gilt:

1. Erklären
2. Aufgabe definieren
3. Umsetzung durchführen
4. Wirksamkeit prüfen
5. Commit erstellen
6. CHANGELOG aktualisieren

Keine Mehrfachänderungen gleichzeitig.

Immer nur einen kontrollierbaren Entwicklungsschritt durchführen.

---

## 11. Aktueller Status

* Version 1.0 veröffentlicht
* GitHub synchronisiert
* Anwendung lauffähig
* Modularisierung begonnen
* Architekturumbau aktiv
* Bereit für weitere Refactoring-Schritte
