# CHANGELOG

## Version 1.0

Ausgangsversion des Projekts.

### Vorhandene Funktionen

* Tkinter-basierte grafische Benutzeroberfläche
* Tab „Einzelerstellung“
* Tab „Sammelverarbeitung“
* Erstellung von Lagerplatzschildern als PDF
* QR-Code-Erzeugung für Lagerplätze
* Unterstützung von 4-Zeilen-Layout
* Unterstützung von 5-Zeilen-Layout
* Firmenlogo im PDF
* PDF-Speicherort-Auswahl
* Excel-basierte Sammelverarbeitung
* Handbuch-Funktion
* Kontakt-/Support-Funktion
* Live-Validierung der Eingabefelder
* Aktivierung des PDF-Buttons nur bei gültigen Eingaben

---

## Version 1.1

### Hinzugefügt

#### Neues Textschild-System

* Neue Funktion `generate_text_sign_pdf()`
* Unterstützung für reine Textschilder ohne QR-Code
* Separater Titelbereich im PDF
* Separater Textbereich im PDF
* Unterstützung von Titel- und Haupttext
* Dynamische Positionierung des Titels
* Dynamische Positionierung des Logos
* Unterstützung für Test-PDFs zur Layoutentwicklung

#### Layoutsystem

* Neues Layoutobjekt `TEXT_SIGN_A4_LANDSCAPE_LAYOUT`
* Definition zentraler Layoutparameter über Dictionary-Konfiguration
* Unterstützung für:

  * Seitenränder
  * Rahmenstärken
  * Logo-Größe
  * Logo-Abstände
  * Titelbereich
  * Textbereich
  * Safe-Area

#### Safe-Area-System

* Einführung eines definierten Textbereiches
* Berechnung einer internen Safe-Area
* Visualisierung der Safe-Area über roten Rahmen
* Optional einblendbare Safe-Area für Entwicklungszwecke
* Trennung zwischen Produktionsansicht und Testansicht

#### Text-Engine

* Automatischer Textumbruch
* Mehrzeilige Darstellung
* Dynamische Zeilenberechnung
* Zentrierte Darstellung aller Textzeilen
* Automatische Schriftgrößenanpassung
* Berücksichtigung von Breite und Höhe der Safe-Area
* Unterstützung langer Textinhalte innerhalb definierter Grenzen

#### GUI

* Neuer Testbutton „Textschild Test“
* Integration der Textschild-PDF-Erstellung in die bestehende GUI
* Erweiterung der Testmöglichkeiten ohne Einfluss auf bestehende Funktionen

---

### Geändert
- `PROJECT_OVERVIEW.md` an die neue PDF-Paketstruktur mit `src/pdf/generator.py` angepasst.
- Aktive Projektverweise auf die alte Datei `pdf_generator.py` geprüft und bereinigt.
- Historische CHANGELOG-Einträge unverändert beibehalten.
- `PROJECT_OVERVIEW.md` an die neue Layout-Struktur mit `src/config/layouts.py` angepasst.
- Aktive Projektverweise auf die alte Datei `src/layouts.py` geprüft und bereinigt.
- Historische CHANGELOG-Einträge unverändert beibehalten.
- `PROJECT_OVERVIEW.md` an die neue Utils-Struktur mit `src/utils/paths.py` angepasst.
- Aktive Projektverweise auf die alte Datei `src/paths.py` geprüft und bereinigt.
- Pfad-Hilfsfunktion `resource_path()` als Bestandteil des Utils-Bereichs dokumentiert.
- `PROJECT_OVERVIEW.md` an die neue Utils-Struktur mit `src/utils/validators.py` angepasst.
- Aktive Projektverweise auf die alte Datei `src/validators.py` geprüft und bereinigt.
- Validierungslogik als Bestandteil des Utils-Bereichs dokumentiert.
- `PROJECT_OVERVIEW.md` an die neue zentrale Batch-PDF-Schnittstelle `generate_batch_pdf()` angepasst.
- Interne Detailfunktionen `generate_batch_pdf_4()` und `generate_batch_pdf_5()` als interne PDF-Funktionen eingeordnet.

#### PDF-Layout

* Logo-Position vollständig neu berechnet
* Logo wird innerhalb des Rahmens positioniert
* Logo überschreitet den Außenrahmen nicht mehr
* Vertikale Position des Logos optimiert
* Oberer Abstand des Logos reduziert
* Titelbereich links neben dem Logo integriert
* Nutzung der oberen freien Fläche ermöglicht

#### Textdarstellung

* Text wird nicht mehr ausschließlich anhand einer festen Schriftgröße dargestellt
* Textgröße wird dynamisch berechnet
* Zeilen werden automatisch erzeugt
* Text wird innerhalb der Safe-Area zentriert

#### Layout-Konfiguration

* Harte Layoutwerte durch zentrale Layoutparameter ersetzt
* Logo- und Titelparameter in Layoutdefinitionen integriert
* Textbereich konfigurierbar vorbereitet

---

### Refactoring

- Klasse `ReleaseNotesWindow` aus `app.py` in das neue GUI-Modul `src/gui/release_notes_window.py` ausgelagert.
- `app.py` weiter reduziert und erste fachliche Trennung innerhalb der GUI-Struktur vorbereitet.
- Importstruktur für das ausgelagerte Release-Notes-Fenster angepasst.
- Klasse `HandbuchWindow` aus `app.py` in das neue GUI-Modul `src/gui/handbuch_window.py` ausgelagert.
- `app.py` weiter reduziert und GUI-Fensterlogik stärker von der Hauptanwendung getrennt.
- Importstruktur für das ausgelagerte Handbuch-Fenster angepasst.
- Neues Konfigurationsmodul `src/config/theme.py` erstellt.
- GUI-Hintergrundfarbe `BG_COLOR` zentralisiert und aus `app.py`, `release_notes_window.py` und `handbuch_window.py` ausgelagert.
- Doppelte Farbdefinitionen reduziert und Grundlage für eine spätere zentrale GUI-Theme-Verwaltung geschaffen.
- GUI-Buttonfarbe `BUTTON_COLOR` in `src/config/theme.py` zentralisiert.
- `app.py` weiter von festen Designwerten entlastet.
- Zentrale Theme-Konfiguration für zukünftige GUI-Anpassungen erweitert.
- Neue Funktion `is_batch_pdf_valid()` in `src/validators.py` ergänzt.
- Batch-Validierung aus `app.py` ausgelagert.
- Validierungslogik für Einzelerstellung und Sammelverarbeitung weiter zentralisiert.
- `app.py` weiter von fachlicher Prüflogik entlastet.
- Neues Hilfsmodul `src/utils/layout_helpers.py` erstellt.
- Funktion `get_line_count_from_layout()` ergänzt.
- Doppelte Logik zur Ermittlung der Zeilenanzahl aus der GUI-Auswahl aus `app.py` ausgelagert.
- Einzelerstellung und Sammelverarbeitung auf die zentrale Hilfsfunktion umgestellt.
- Batch-PDF-Methoden `generate_pdf_4()` und `generate_pdf_5()` auf explizite Parameterübergabe umgestellt.
- Direkte Abhängigkeit der Batch-PDF-Erzeugung von Tkinter-Eingabefeldern reduziert.
- Methode `on_batch_generate()` übergibt Excel- und PDF-Ausgabepfad nun gezielt an die PDF-Erzeugung.
- Auslagerung der Batch-PDF-Erzeugung aus `app.py` vorbereitet.
- 4-Zeilen-Batch-PDF-Erzeugung aus `app.py` nach `src/pdf_generator.py` ausgelagert.
- Neue Funktion `generate_batch_pdf_4(excel, output)` erstellt.
- GUI-Klasse `QRCodeGeneratorApp` weiter von PDF-Erzeugungslogik entlastet.
- Sammelverarbeitung für 4-Zeilen-Layouts nach Auslagerung erfolgreich geprüft.
- 5-Zeilen-Batch-PDF-Erzeugung aus `app.py` nach `src/pdf_generator.py` ausgelagert.
- Neue Funktion `generate_batch_pdf_5(excel, output)` erstellt.
- Batch-PDF-Erzeugung vollständig aus der GUI-Klasse `QRCodeGeneratorApp` entfernt.
- `app.py` weiter auf GUI-Steuerung und Benutzerinteraktion reduziert.
- Sammelverarbeitung für 4- und 5-Zeilen-Layouts nach Auslagerung erfolgreich geprüft.
- Nicht mehr benötigte Imports aus `app.py` entfernt.
- Veraltete Abhängigkeiten zu Excel-, QR-Code-, PDF- und Systembibliotheken aus der GUI-Datei bereinigt.
- `app.py` weiter auf GUI-Steuerung und Benutzerinteraktion reduziert.
- Logo-Anzeige nach Korrektur des verwendeten Asset-Namens erfolgreich geprüft.
- Doppelte GUI-Logo-Logik aus `build_tab_single()` und `build_tab_batch()` entfernt.
- Neue Methode `add_logo_to_frame()` in `QRCodeGeneratorApp` ergänzt.
- Logo-Erstellung und Logo-Platzierung innerhalb der GUI zentralisiert.
- Anzeige des Firmenlogos in beiden Tabs erfolgreich geprüft.
- GUI-Logo-Konfiguration in `src/config/theme.py` zentralisiert.
- Logo-Dateiname, Logo-Größe und Logo-Position aus `app.py` ausgelagert.
- Methode `add_logo_to_frame()` auf zentrale Konfigurationswerte umgestellt.
- Logo-Anzeige in beiden Tabs nach der Umstellung erfolgreich geprüft.
- PDF-Funktionsimporte in `app.py` gebündelt.
- Mehrere Einzelimporte aus `src.pdf_generator` durch einen übersichtlichen mehrzeiligen Import ersetzt.
- Importstruktur in `app.py` weiter bereinigt.
- Neue Datei `src/gui/__init__.py` erstellt.
- GUI-Fenster `ReleaseNotesWindow` und `HandbuchWindow` zentral über `src.gui` exportiert.
- Importstruktur in `app.py` für GUI-Komponenten vereinfacht.
- Grundlage für weitere GUI-Modularisierung geschaffen.
- Neue Datei `src/config/__init__.py` erstellt.
- Theme- und GUI-Logo-Konfigurationswerte zentral über `src.config` exportiert.
- Importstruktur in `app.py` für Konfigurationswerte vereinfacht.
- Grundlage für weitere Konfigurationsmodule geschaffen.
- Neue Datei `src/utils/__init__.py` erstellt.
- Hilfsfunktion `get_line_count_from_layout()` zentral über `src.utils` exportiert.
- Importstruktur in `app.py` für Hilfsfunktionen vereinfacht.
- Grundlage für weitere Utility-Module geschaffen.
- Neues Paket `src/pdf/` erstellt.
- Datei `pdf_generator.py` nach `src/pdf/generator.py` verschoben.
- Neue Datei `src/pdf/__init__.py` erstellt.
- PDF-Funktionen zentral über `src.pdf` exportiert.
- Importstruktur in `app.py` auf das neue PDF-Paket umgestellt.
- Einzelerstellung, Textschild-Test, Sammelverarbeitung, Handbuch, Release Notes und Logo nach der Umstellung erfolgreich geprüft.
- Layoutdefinitionen aus `src/layouts.py` nach `src/config/layouts.py` verschoben.
- Import der Layoutdefinitionen im PDF-Generator auf `src.config.layouts` angepasst.
- Layoutwerte fachlich dem Konfigurationsbereich zugeordnet.
- PDF-Erzeugung und GUI-Funktionen nach der Umstellung erfolgreich geprüft.
- Datei `paths.py` nach `src/utils/paths.py` verschoben.
- Funktion `resource_path()` zentral über `src.utils` exportiert.
- Imports in `app.py` und `src/pdf/generator.py` angepasst.
- Pfadlogik fachlich dem Utils-Bereich zugeordnet.
- GUI-Logo und PDF-Erzeugung nach der Umstellung erfolgreich geprüft.
- Datei `validators.py` nach `src/utils/validators.py` verschoben.
- Funktionen `is_single_pdf_valid()` und `is_batch_pdf_valid()` zentral über `src.utils` exportiert.
- Imports in `app.py` angepasst.
- Validierungslogik fachlich dem Utils-Bereich zugeordnet.
- Button-Validierung für Einzelerstellung und Sammelverarbeitung nach der Umstellung erfolgreich geprüft.
- Neues Verzeichnis `src/services/` erstellt.
- Support-Mail-Logik aus `app.py` in `src/services/support_service.py` ausgelagert.
- Neue Funktion `open_support_email()` erstellt.
- Methode `open_email()` in `app.py` auf einen Service-Aufruf reduziert.
- Support-Button nach der Umstellung erfolgreich geprüft.
- Neue Datei `src/services/__init__.py` erstellt.
- Funktion `open_support_email()` zentral über `src.services` exportiert.
- Importstruktur in `app.py` für Service-Funktionen vereinfacht.
- Grundlage für weitere Service-Module geschaffen.
- Neue Funktion `generate_batch_pdf()` in `src/pdf/generator.py` ergänzt.
- Auswahl zwischen `generate_batch_pdf_4()` und `generate_batch_pdf_5()` in das PDF-Modul verlagert.
- `app.py` auf zentralen Batch-PDF-Aufruf umgestellt.
- Direkte Detailaufrufe der 4- und 5-Zeilen-Batch-Erzeugung aus der GUI entfernt.
- Sammelverarbeitung für beide Layoutvarianten nach der Umstellung erfolgreich geprüft.
- Öffentliche Exporte in `src/pdf/__init__.py` bereinigt.
- Detailfunktionen `generate_batch_pdf_4()` und `generate_batch_pdf_5()` nicht mehr über `src.pdf` exportiert.
- `generate_batch_pdf()` als zentrale öffentliche Batch-PDF-Schnittstelle beibehalten.
- PDF-Paket-Schnittstelle weiter vereinfacht.
- Neue Datei `src/__init__.py` erstellt.
- `src` als zentrales Python-Paket gekennzeichnet.
- Bestehende Paketstruktur formal vervollständigt.
- Hauptfensterklasse `QRCodeGeneratorApp` aus `src/app.py` nach `src/gui/main_window.py` verschoben.
- `src/app.py` auf die reine Startlogik der Anwendung reduziert.
- GUI-Paketstruktur durch zentrale Hauptfenster-Datei erweitert.
- GUI-Konstanten für Fenstergröße, Separator-Farbe und Versionslabel nach `src/config/theme.py` ausgelagert.
- Harte GUI-Werte in `src/gui/main_window.py` durch zentrale Konfigurationswerte ersetzt.
- Öffentliche Konfigurationsschnittstelle über `src/config/__init__.py` erweitert.
- Zentrale GUI-Schriftdefinitionen in `src/config/theme.py` ergänzt.
- Wiederkehrende Schriftwerte in `src/gui/main_window.py` durch zentrale Theme-Konstanten ersetzt.
- Öffentliche Konfigurationsschnittstelle über `src/config/__init__.py` um GUI-Schriftwerte erweitert.
- Hinweistext-Schrift und Hinweistext-Farbe als zentrale Theme-Konstanten ergänzt.
- Drei Hinweiszeilen im Tab „Sammelverarbeitung“ auf zentrale Theme-Werte umgestellt.

#### Neue Datei: layouts.py

Ausgelagert:

* Layoutdefinitionen
* PDF-Konfigurationen
* Größenparameter
* Safe-Area-Konfigurationen

Enthält:

* Lagerplatzlayouts
* Textschildlayouts

#### Neue Datei: validators.py

Ausgelagert:

* Validierungslogik

Enthält:

* `is_single_pdf_valid()`

#### Neue Datei: paths.py

Ausgelagert:

* Ressourcenverwaltung

Enthält:

* `resource_path()`

#### Architekturverbesserungen

* Reduzierung von Hardcodierungen
* Zentrale Verwaltung von Layoutparametern
* Vorbereitung weiterer Schildtypen
* Verbesserte Trennung von GUI, Layout und PDF-Erzeugung

---

### Behoben

#### Importfehler

Behoben:

* `ModuleNotFoundError: No module named 'src'`
* fehlerhafte Modulimporte
* fehlerhafte PIL-Importe
* fehlerhafte ReportLab-Aufrufe

#### Logo-Probleme

Behoben:

* Logo außerhalb des Rahmens
* Logo überlappte Safe-Area
* fehlerhafte Logo-Abstände
* fehlerhafte Berechnung der Logo-Position

#### Textdarstellung

Behoben:

* Text außerhalb der Safe-Area
* Textüberschreitungen bei langen Inhalten
* fehlerhafte Zentrierung
* fehlerhafte Schriftgrößenberechnung

#### GUI-Probleme

Behoben:

* fehlerhafte Button-Integration
* Aktivierungsprobleme von Buttons
* fehlerhafte Callback-Aufrufe

#### Python-Fehler

Behoben:

* SyntaxError
* NameError
* TypeError
* AttributeError
* ImportError
* IndentationError

Konkret:

* `font_size not defined`
* `title_text not defined`
* falsche Parameteranzahl bei `generate_text_sign_pdf()`
* fehlerhafte Einrückungen
* fehlende Klammern
* fehlerhafte Variablennamen

#### Safe-Area-Berechnung

Behoben:

* Berechnung an falscher Stelle im Code
* falsche Reihenfolge der Berechnungen
* fehlerhafte Größenberechnung

---

### Technische Änderungen

#### PDF-Erstellung

Verwendete Bibliotheken:

* ReportLab
* Pillow

#### GUI

Verwendete Bibliotheken:

* Tkinter
* ttk

#### QR-Code

Verwendete Bibliotheken:

* qrcode

#### Excel-Verarbeitung

Verwendete Bibliotheken:

* openpyxl

#### Layout-Engine

Neu eingeführt:

* Berechnung von Textbreiten über `pdfmetrics.stringWidth()`
* Dynamische Schriftgrößenreduktion
* Dynamische Zeilenaufteilung
* Zentrierungslogik

---

### Projektstruktur

Aktive Kernmodule und Pakete:

* `main.py`
* `src/app.py`

#### GUI

* `src/gui/__init__.py`
* `src/gui/release_notes_window.py`
* `src/gui/handbuch_window.py`

#### PDF

* `src/pdf/__init__.py`
* `src/pdf/generator.py`

#### Konfiguration

* `src/config/__init__.py`
* `src/config/theme.py`
* `src/config/layouts.py`

#### Services

* `src/services/__init__.py`
* `src/services/support_service.py`

#### Utilities

* `src/utils/__init__.py`
* `src/utils/layout_helpers.py`
* `src/utils/paths.py`
* `src/utils/validators.py`

Verwendete Ressourcen:

* Firmenlogo
* PDF-Ausgabeordner
* GUI-Komponenten

---

### Bekannte Einschränkungen

* Nur A4 Querformat implementiert
* Textschildfunktion derzeit über Testbutton erreichbar
* Keine integrierte Vorschau innerhalb der GUI
* Nur zentrierte Textausrichtung implementiert
* Keine manuelle Schriftartauswahl
* Keine manuelle Schriftgrößensteuerung
* Keine Unterstützung für Hochformat
* Keine Unterstützung für A3 oder A5
* Safe-Area dient aktuell primär der Entwicklung und Qualitätssicherung
* Textumbruch erfolgt aktuell wortbasiert und noch nicht über eine vollständige Layout-Optimierungslogik
* Vorschaufenster noch nicht implementiert
* Weitere Schildtypen noch nicht integriert

