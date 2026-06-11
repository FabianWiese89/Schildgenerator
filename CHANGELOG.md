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
- Fenstertitel und Tab-Namen als zentrale Theme-Konstanten ergänzt.
- Hauptfenster-Strukturtexte in `src/gui/main_window.py` auf zentrale Konfigurationswerte umgestellt.
- Harte Strukturtexte im Hauptfenster weiter reduziert.
- Status- und Versionsfarben als zentrale Theme-Konstanten ergänzt.
- Statuslabel und Versionslabel im Hauptfenster auf zentrale Farbwerte umgestellt.
- Harte Farbangaben für Status- und Versionsanzeige in `src/gui/main_window.py` reduziert.
- Button-Textfarbe als zentrale Theme-Konstante `BUTTON_TEXT_COLOR` ergänzt.
- Button-Schriftfarben im Hauptfenster auf zentrale Theme-Werte umgestellt.
- Harte Button-Farbwerte in `src/gui/main_window.py` weiter reduziert.
- Entry-Textfarbe und Entry-Cursorfarbe als zentrale Theme-Konstanten ergänzt.
- Eingabefelder im Hauptfenster auf zentrale Theme-Werte umgestellt.
- Harte Entry-Farbwerte in `src/gui/main_window.py` weiter reduziert.
- Layout-Auswahltexte für die GUI als zentrale Konfigurationswerte ergänzt.
- Standardwert und Auswahloptionen der Layout-Dropdowns in `src/gui/main_window.py` auf zentrale Werte umgestellt.
- Harte Layout-Auswahltexte im Hauptfenster reduziert.
- Gültige Layout-Auswahlwerte als zentrale Konfigurationsliste `VALID_LAYOUT_OPTIONS` ergänzt.
- Validierungslogik für Einzelerstellung und Sammelverarbeitung auf zentrale Layout-Konstanten umgestellt.
- Harte Layout-Auswahltexte aus `src/utils/validators.py` entfernt.
- Funktion `get_line_count_from_layout()` auf zentrale Layout-Konstanten umgestellt.
- Textfragment-Prüfung in `src/utils/layout_helpers.py` durch exakte Layoutwert-Vergleiche ersetzt.
- Rückgabeverhalten bei ungültiger Layout-Auswahl klarer definiert.
- Veraltete Kommentare in `src/gui/main_window.py` bereinigt.
- Abschnittsbezeichnung für das Hauptfenster aktualisiert.
- Nicht mehr passende Batch-Kommentarzeile nach Auslagerung der PDF-Erzeugung entfernt.
- Gemeinsame Handbuch-Aktion `show_handbuch()` innerhalb von `src/gui/main_window.py` in den Bereich gemeinsamer Aktionen verschoben.
- Methodenstruktur im Hauptfenster fachlich klarer gruppiert.
- Vorbereitung für spätere Auslagerung von Einzelerstellung und Sammelverarbeitung verbessert.
- Versionslabel- und Release-Notes-Bereich in `src/gui/main_window.py` klarer gruppiert.
- Methode `add_logo_to_frame()` in einen allgemeinen GUI-Hilfsmethodenbereich verschoben.
- Abschnittsstruktur im Hauptfenster für spätere GUI-Auslagerungen weiter vorbereitet.
- Versionslabel- und Release-Notes-Bereich in `src/gui/main_window.py` klarer gruppiert.
- Methode `add_logo_to_frame()` in einen allgemeinen GUI-Hilfsmethodenbereich verschoben.
- Abschnittsstruktur im Hauptfenster für spätere GUI-Auslagerungen weiter vorbereitet.
- Initialisierung der Einzelerstellungs-Variablen in `init_single_variables()` ausgelagert.
- Initialisierung der Sammelverarbeitungs-Variablen in `init_batch_variables()` ausgelagert.
- `__init__` der Hauptfensterklasse weiter entschlackt und fachlich klarer strukturiert.
- Labeltexte der Einzelerstellung als zentrale Konfigurationswerte ergänzt.
- Beschriftungen im Tab „Einzelerstellung“ in `src/gui/main_window.py` auf zentrale Textkonstanten umgestellt.
- Vorbereitung für spätere Auslagerung des Einzelerstellungs-Tabs verbessert.
- Labeltexte der Sammelverarbeitung als zentrale Konfigurationswerte ergänzt.
- Beschriftungen im Tab „Sammelverarbeitung“ in `src/gui/main_window.py` auf zentrale Textkonstanten umgestellt.
- Vorbereitung für spätere Auslagerung des Sammelverarbeitungs-Tabs verbessert.
- Buttontexte als zentrale Konfigurationswerte ergänzt.
- Wiederkehrende Button-Beschriftungen in `src/gui/main_window.py` auf zentrale Textkonstanten umgestellt.
- Vorbereitung für spätere Auslagerung von Einzelerstellung und Sammelverarbeitung weiter verbessert.
- Status- und Erfolgsmeldungen als zentrale Konfigurationswerte ergänzt.
- Statusanzeigen für Einzelerstellung und Sammelverarbeitung auf zentrale Textkonstanten umgestellt.
- Erfolgsmeldungen der PDF-Erstellung in `src/gui/main_window.py` auf zentrale Meldungstexte umgestellt.
- Dateidialog-Texte und Dateityp-Filter als zentrale Konfigurationswerte ergänzt.
- PDF-Speicherdialoge in Einzelerstellung und Sammelverarbeitung auf zentrale Dialog-Konstanten umgestellt.
- Excel-Auswahldialog der Sammelverarbeitung auf zentrale Dialog-Konstanten umgestellt.
- Harte Dateidialog-Werte in `src/gui/main_window.py` reduziert.
- Hinweistexte der Sammelverarbeitung als zentrale Konfigurationswerte ergänzt.
- Hinweislabels im Tab „Sammelverarbeitung“ auf zentrale Textkonstanten umgestellt.
- Harte Hinweistext-Werte in `src/gui/main_window.py` weiter reduziert.
- Textschild-Testbutton als temporäre Entwicklungsfunktion gekennzeichnet.
- Zentrale Konfiguration `SHOW_TEXT_SIGN_TEST_BUTTON` ergänzt.
- Testbutton kann nun ohne Code-Löschung zentral ein- oder ausgeblendet werden.
- GUI-Imports in `src/gui/main_window.py` präzisiert.
- Direkte Modulimporte für `ReleaseNotesWindow` und `HandbuchWindow` ergänzt.
- Abhängigkeit des Hauptfensters vom GUI-Paketexport reduziert.
- Ausgewählte Notebook-Tab-Farbe als zentrale Theme-Konstante ergänzt.
- Harten Farbwert für den aktiven Tab in `src/gui/main_window.py` entfernt.
- GUI-Theme-Konfiguration weiter vervollständigt.
- Handbuch-Button-Erstellung in zentrale GUI-Hilfsmethode `add_handbook_button()` ausgelagert.
- Doppelte Handbuch-Button-Logik aus Einzelerstellung und Sammelverarbeitung entfernt.
- Hauptfensterstruktur weiter für spätere Tab-Auslagerung vorbereitet.
- Kontakt-/Support-Button-Erstellung in zentrale GUI-Hilfsmethode `add_support_button()` ausgelagert.
- Doppelte Support-Button-Logik aus Einzelerstellung und Sammelverarbeitung entfernt.
- Gemeinsame GUI-Buttonlogik im Hauptfenster weiter reduziert.
- Durchsuchen-Button-Erstellung in zentrale GUI-Hilfsmethode `add_browse_button()` ausgelagert.
- Wiederholte Browse-Button-Logik in Einzelerstellung und Sammelverarbeitung reduziert.
- Gemeinsame GUI-Buttonlogik im Hauptfenster weiter vereinheitlicht.
- PDF-Erstellen-Button-Erstellung in zentrale GUI-Hilfsmethode `add_create_pdf_button()` ausgelagert.
- Wiederholte PDF-Button-Logik in Einzelerstellung und Sammelverarbeitung reduziert.
- Gemeinsame GUI-Buttonlogik im Hauptfenster weiter vereinheitlicht.
- Statuslabel-Erstellung in zentrale GUI-Hilfsmethode `add_status_label()` ausgelagert.
- Doppelte Statuslabel-Logik aus Einzelerstellung und Sammelverarbeitung reduziert.
- Gemeinsame GUI-Element-Erzeugung im Hauptfenster weiter vereinheitlicht.
- Layout-Combobox-Erstellung in zentrale GUI-Hilfsmethode `add_layout_combobox()` ausgelagert.
- Wiederholte Layout-Dropdown-Logik in Einzelerstellung und Sammelverarbeitung reduziert.
- Eingabefeld-Erstellung in zentrale GUI-Hilfsmethode `add_text_entry()` ausgelagert.
- Wiederholte Entry-Logik im Hauptfenster reduziert.
- Status- und Buttonplatzierung nach der GUI-Hilfsmethoden-Auslagerung korrigiert.

- Oberflächenaufbau der Einzelerstellung in `src/gui/single_tab.py` ausgelagert.
- `build_tab_single()` in `src/gui/main_window.py` auf einen delegierenden Aufruf reduziert.
- Oberflächenaufbau der Sammelverarbeitung in `src/gui/batch_tab.py` ausgelagert.
- `build_tab_batch()` in `src/gui/main_window.py` auf einen delegierenden Aufruf reduziert.
- Hauptfenster weiter von direkter Tab-Aufbaulogik entlastet.
- Vorbereitung für spätere fachliche Trennung von GUI-Aufbau und Steuerungslogik verbessert.
- Steuerungslogik der Einzelerstellung in `src/gui/single_actions.py` ausgelagert.
- Methoden `update_single_button()`, `single_save_pdf()` und `on_single_generate()` in `src/gui/main_window.py` auf delegierende Aufrufe reduziert.
- Hauptfenster weiter von fachlicher Einzelerstellungslogik entlastet.
- Vorbereitung für die anschließende Auslagerung der Sammelverarbeitungslogik verbessert.
- Steuerungslogik der Sammelverarbeitung in `src/gui/batch_actions.py` ausgelagert.
- Methoden `update_batch_button()`, `browse_batch_excel()`, `save_batch_pdf()` und `on_batch_generate()` in `src/gui/main_window.py` auf delegierende Aufrufe reduziert.
- Hauptfenster weiter von fachlicher Sammelverarbeitungslogik entlastet.
- Trennung zwischen GUI-Aufbau und Steuerungslogik für beide Tabs vervollständigt.

- Gemeinsame GUI-Hilfsfunktionen in `src/gui/gui_helpers.py` ausgelagert.
- Logo-, Handbuch-, Support-, Browse-, Layout-, PDF-Button-, Statuslabel- und Eingabefeld-Helfer aus `src/gui/main_window.py` entlastet.
- `src/gui/main_window.py` weiter auf Hauptfenstersteuerung und delegierende Methoden reduziert.
- Wiederverwendbare GUI-Bausteine fachlich in ein eigenes Hilfsmodul verschoben.

- GUI-Paketimporte bereinigt: `src/app.py` importiert `QRCodeGeneratorApp` nun direkt aus `src/gui/main_window.py`.
- `src/gui/__init__.py` von schweren Re-Exports entlastet und auf eine reine Paketdatei reduziert.
- Importstruktur der GUI weiter vereinfacht und potenzielle Paket-Import-Nebeneffekte reduziert.

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
* `src/gui/main_window.py`
* `src/gui/single_tab.py`
* `src/gui/single_actions.py`
* `src/gui/batch_tab.py`
* `src/gui/batch_actions.py`
* `src/gui/gui_helpers.py`
* `src/gui/release_notes_window.py`
* `src/gui/handbuch_window.py`

#### PDF

* `src/pdf/__init__.py`
* `src/pdf/generator.py`

#### Konfiguration

* `src/config/__init__.py`
* `src/config/theme.py`
* `src/config/layouts.py`

Zentralisierte Konfigurationsbereiche:

* Layoutwerte
* Theme-Farben
* GUI-Schriften
* GUI-Textwerte
* Buttontexte
* Status- und Dialogtexte
* Dateidialog-Filter

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

