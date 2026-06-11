# Lagerplatz-QRCode-Generator

Lokales Python-Programm zur Erstellung von Lagerplatzschildern mit QR-Code als PDF.

Das Projekt wird schrittweise zu einem modularen Schildgenerator für Lager, Logistik und industrielle Anwendungen weiterentwickelt.

---

## Aktueller Funktionsumfang

Aktuell unterstützt das Programm:

* Einzelerstellung von Lagerplatzschildern
* Sammelverarbeitung über Excel
* QR-Code-Erstellung
* PDF-Ausgabe
* Auswahl zwischen 4-Zeilen- und 5-Zeilen-Layout
* Firmenlogo im PDF
* Grafische Oberfläche mit Tkinter
* Handbuch-Funktion
* Kontakt-/Support-Funktion
* Textschild-Testfunktion zur Layoutentwicklung

---

## Projektziel

Langfristig soll aus dem ursprünglichen Lagerplatz-QRCode-Generator ein flexibler Schildgenerator entstehen.

Geplante Einsatzbereiche:

* Lagerplatzschilder
* QR-Code-Schilder
* Textschilder
* Sicherheitsschilder
* Parkplatzschilder
* Bereichsschilder

Der aktuelle Fokus liegt jedoch nicht auf neuen Funktionen, sondern auf:

* sauberer Projektstruktur
* Modularisierung
* Wartbarkeit
* klarer Trennung von GUI, PDF-Erzeugung, Konfiguration, Services und Hilfsfunktionen

---

## Projektstruktur

Die aktuelle Kernstruktur:

```text
src/
├── app.py
├── config/
│   ├── layouts.py
│   └── theme.py
├── gui/
│   ├── main_window.py
│   ├── single_tab.py
│   ├── batch_tab.py
│   ├── handbuch_window.py
│   └── release_notes_window.py
├── pdf/
│   └── generator.py
├── services/
│   └── support_service.py
└── utils/
    ├── layout_helpers.py
    ├── paths.py
    └── validators.py
```

---

## Installation

Benötigt wird Python 3.

Abhängigkeiten installieren:

```powershell
pip install openpyxl qrcode reportlab pillow
```

Falls eine virtuelle Umgebung verwendet wird:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install openpyxl qrcode reportlab pillow
```

---

## Programm starten

Im Projektordner ausführen:

```powershell
python main.py
```

---

## Entwicklungsstand

Aktuelle Phase:

```text
Phase 1: Architektur und Modularisierung
```

Der Schwerpunkt liegt aktuell auf:

* Aufräumen der Projektstruktur
* Auslagern von Modulen
* Reduzieren von Hardcodierungen
* Vereinfachen von Importstrukturen
* Stabilisieren der bestehenden Funktionen

Neue Funktionen werden erst nach Abschluss der Grundstruktur priorisiert.

---

## Dokumentation

Weitere Projektdokumentation:

* `PROJECT_OVERVIEW.md`
* `CHANGELOG.md`

---

## Status

Das Projekt ist lauffähig und wird aktiv weiterentwickelt.
