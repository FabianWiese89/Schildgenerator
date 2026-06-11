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

Ausgelagerte Komponenten und Pakete:

* `src/gui/`
  * `main_window.py`
  * `single_tab.py`
  * `single_actions.py`
  * `batch_tab.py`
  * `batch_actions.py`
  * `gui_helpers.py`
  * `release_notes_window.py`
  * `handbuch_window.py`
  * Paketdatei `src/gui/__init__.py` ohne schwere Re-Exports

* `src/pdf/`
  * `generator.py`
  * zentraler Export der PDF-Funktionen über `src/pdf/__init__.py`

* `src/config/`
  * `theme.py`
  * `layouts.py`
  * zentraler Export der Theme-, Layout-, Logo- und GUI-Textkonfiguration über `src/config/__init__.py`

* `src/utils/`
  * `layout_helpers.py`
  * `paths.py`
  * `validators.py`
  * zentraler Export über `src/utils/__init__.py`

* `src/services/`
  * `support_service.py`
  * zentraler Export über `src/services/__init__.py`

Neue bzw. ausgelagerte öffentliche Funktionen:

* `generate_text_sign_pdf()`
* `generate_batch_pdf()`
* `get_line_count_from_layout()`
* `resource_path()`
* `is_single_pdf_valid()`
* `is_batch_pdf_valid()`
* `open_support_email()`

Interne Detailfunktionen:

* `generate_batch_pdf_4()`
* `generate_batch_pdf_5()`

---

## 5. Wichtige Dateien und Pakete

Aktuell:

* `main.py`
* `src/app.py`
* `src/__init__.py`

### GUI

* `src/gui/__init__.py`
* `src/gui/main_window.py`
* `src/gui/single_tab.py`
* `src/gui/single_actions.py`
* `src/gui/batch_tab.py`
* `src/gui/batch_actions.py`
* `src/gui/gui_helpers.py`
* `src/gui/release_notes_window.py`
* `src/gui/handbuch_window.py`

### PDF

* `src/pdf/__init__.py`
* `src/pdf/generator.py`

### Konfiguration

* `src/config/__init__.py`
* `src/config/theme.py`
* `src/config/layouts.py`

### Services

* `src/services/__init__.py`
* `src/services/support_service.py`

### Dokumentation

* `docs/PROJECT_STRUCTURE_REVIEW.md`

### Utilities

* `src/utils/__init__.py`
* `src/utils/layout_helpers.py`
* `src/utils/paths.py`
* `src/utils/validators.py`

---

## 5.1 Aktuelle Projektstruktur

```text
src/
├── __init__.py
├── app.py
├── config/
│   ├── __init__.py
│   ├── layouts.py
│   └── theme.py
├── gui/
│   ├── __init__.py
│   ├── batch_tab.py
│   ├── batch_actions.py
│   ├── gui_helpers.py
│   ├── handbuch_window.py
│   ├── main_window.py
│   ├── release_notes_window.py
│   ├── single_actions.py
│   └── single_tab.py
├── pdf/
│   ├── __init__.py
│   └── generator.py
├── services/
│   ├── __init__.py
│   └── support_service.py
└── utils/
    ├── __init__.py
    ├── layout_helpers.py
    ├── paths.py
    └── validators.py
```

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
* Version 1.1 als Architektur- und Modularisierungsstand vorbereitet
* GitHub synchronisiert
* Anwendung lauffähig
* Modularisierung begonnen
* Architekturumbau aktiv
* Bereit für weitere Refactoring-Schritte
* Hauptfensterklasse `QRCodeGeneratorApp` nach `src/gui/main_window.py` ausgelagert
* Oberflächenaufbau der Einzelerstellung nach `src/gui/single_tab.py` ausgelagert
* Steuerungslogik der Einzelerstellung nach `src/gui/single_actions.py` ausgelagert
* Oberflächenaufbau der Sammelverarbeitung nach `src/gui/batch_tab.py` ausgelagert
* Steuerungslogik der Sammelverarbeitung nach `src/gui/batch_actions.py` ausgelagert
* Gemeinsame GUI-Hilfsfunktionen nach `src/gui/gui_helpers.py` ausgelagert
* GUI-Paketimporte wurden bereinigt und `src/gui/__init__.py` dient nur noch als Paketdatei
* `src/gui/main_window.py` wurde strukturell bereinigt und stärker auf Hauptfenster-Aufbau sowie delegierende Methoden reduziert
* Projektstruktur-Review durchgeführt und technische Artefakte wie `__pycache__`, virtuelle Umgebungen und versehentliche Doppelstrukturen als nicht versionierbar eingeordnet
* PDF-Erzeugung nach `src/pdf/` verschoben
* Layout- und Theme-Konfiguration nach `src/config/` verschoben
* Pfad-, Layout- und Validierungshelfer nach `src/utils/` verschoben
* Support-Mail-Logik nach `src/services/` ausgelagert
* Paket-Exports über `__init__.py` für `gui`, `pdf`, `config`, `utils` und `services` eingerichtet
* GUI-Theme-, Text- und Dialogwerte in `src/config/theme.py` zentralisiert
* Textschild-Testbutton als temporäre Entwicklungsfunktion zentral ein- und ausblendbar
* Versionsanzeige im Programm auf Version 1.1 aktualisiert
* Fenstertitel auf Version 1.1 aktualisiert
* PDF-Footer auf Version 1.1 aktualisiert
* Release Notes im Programm um Version 1.1 ergänzt