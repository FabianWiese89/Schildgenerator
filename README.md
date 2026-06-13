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

Der aktuelle Fokus liegt jedoch nicht auf neuen Funktionen, sondern auf Stabilität und Wartbarkeit:

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
│   ├── single_actions.py
│   ├── batch_tab.py
│   ├── batch_actions.py
│   ├── gui_helpers.py
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

Die Anwendung importiert GUI-Komponenten direkt aus ihren jeweiligen Modulen. `src/gui/__init__.py` dient als Paketdatei und enthält keine schweren Re-Exports mehr.

`src/gui/main_window.py` wurde einem Stabilitäts-Review unterzogen und ist jetzt stärker auf Hauptfenster-Aufbau, Versionsanzeige und delegierende Methoden fokussiert. Zusätzlich wurde ein Projektstruktur-Review durchgeführt; technische Artefakte wie `__pycache__`, virtuelle Umgebungen und versehentliche Doppelstrukturen sollen nicht versioniert werden.

---

## Installation

Benötigt wird Python 3.

Empfohlen ist die Installation über `requirements.txt`:

```powershell
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

Alternativ können die Abhängigkeiten manuell installiert werden:

```powershell
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
* `docs/PROJECT_STRUCTURE_REVIEW.md`
* `docs/TESTPLAN.md`
* `docs/SETUP_AND_TROUBLESHOOTING.md`
* `docs/VERSION_1_2_STABILISIERUNG.md`

---

## Status

Das Projekt ist als **Version 1.2 – Stabilisierung** vorbereitet.

Version 1.2 bündelt robustere Pfad- und Datei-Prüfungen, verständlichere Fehlermeldungen, stabilere PDF-Erzeugung ohne temporäre Bilddateien, abgesicherte Excel-Sammelverarbeitung sowie aktualisierte Release Notes im Programm.
