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