# PROJECT_OVERVIEW.md

# Projektübersicht

## 1. Projektziel
Das Projekt ist ein Python-basierter Lagerplatz- und Schildgenerator mit grafischer Benutzeroberfläche (Tkinter).

Ziel ist die Erstellung professioneller Lagerplatzschilder, QR-Code-Schilder und künftig allgemeiner Text-, Sicherheits-, Parkplatz- und Bereichsschilder.

## 2. Bereits vorhandene Funktionen
- QR-Code-Erzeugung
- PDF-Erzeugung
- 4-Zeilen Layout
- 5-Zeilen Layout
- Firmenlogo
- Rahmen
- Batch-Verarbeitung
- GUI mit Tabs
- Handbuch-Button
- Kontakt-/Support-Button

## 3. Umgesetzte Anpassungen
- validators.py ausgelagert
- layouts.py eingeführt
- paths.py eingeführt
- generate_text_sign_pdf() entwickelt
- Safe-Area-System entwickelt
- Automatische Schriftgrößenanpassung
- Automatischer Textumbruch
- Zentrierung mehrerer Zeilen

## 4. GUI-Entscheidungen
Aktuell:
- Einzelerstellung
- Sammelverarbeitung
- Testbutton für Textschild

Geplant:
- Titel-Eingabe
- Text-Eingabe
- Schriftart
- Schriftgröße
- Ausrichtung
- Vorschaufenster
- Safe-Area Ein/Aus

## 5. PDF-Entscheidungen
Aktuell:
- A4 Querformat

Später:
- A3/A4/A5
- Hoch-/Querformat

Layout:
- Rahmen
- Logo oben rechts
- Titel oben links
- Text-Safe-Area

## 6. Wichtige Dateien
- main.py
- app.py
- pdf_generator.py
- validators.py
- layouts.py
- paths.py

## 7. Bibliotheken
- Tkinter
- ReportLab
- Pillow
- qrcode
- openpyxl

## 8. Gelöste Fehler
- Logo-Pfad korrigiert
- Importfehler behoben
- font_size Fehler behoben
- Safe-Area Berechnung korrigiert
- Button-Validierung ausgelagert

## 9. Empfohlene Zielstruktur

src/
├── gui/
├── pdf/
├── engine/
├── layout/
├── utils/
├── assets/
├── docs/
├── tests/

## 10. Nächste Schritte
1. Text-Engine vervollständigen
2. Ausrichtungen einbauen
3. GUI erweitern
4. Vorschaufenster entwickeln
5. Formatverwaltung A3/A4/A5
6. Weitere Schildtypen

## Aktueller Status
- Stabil
- GitHub synchronisiert
- Text-Engine funktionsfähig
- Modularisierung begonnen
- Bereit für weitere Codex-Entwicklung
