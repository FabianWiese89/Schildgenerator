# TESTPLAN

## Zweck

Dieser Testplan beschreibt die wichtigsten manuellen Prüfungen für den Schildgenerator.

Er dient dazu, nach Refactorings, Fehlerbehebungen oder Versionsanpassungen schnell und nachvollziehbar zu prüfen, ob die Anwendung weiterhin stabil läuft.

---

## Grundprüfung

| Nr. | Test | Erwartetes Ergebnis |
|---:|---|---|
| 1 | Anwendung mit `python main.py` starten | Hauptfenster öffnet ohne Fehlermeldung |
| 2 | Fenstertitel prüfen | Fenstertitel zeigt die aktuelle Version |
| 3 | Versionslabel unten links prüfen | Versionslabel zeigt die aktuelle Version |
| 4 | Versionslabel anklicken | Release Notes öffnen sich |
| 5 | Handbuch-Button anklicken | Handbuchfenster öffnet sich |
| 6 | Kontakt-/Support-Button anklicken | E-Mail-Programm bzw. Mail-Dialog öffnet sich |

---

## Einzelerstellung

| Nr. | Test | Erwartetes Ergebnis |
|---:|---|---|
| 1 | Tab „Einzelerstellung“ öffnen | Tab wird korrekt angezeigt |
| 2 | 4-Zeilen-Layout auswählen | Layoutauswahl wird übernommen |
| 3 | Lagerplatztext eintragen | Eingabe wird angenommen |
| 4 | PDF-Speicherort auswählen | Pfad wird übernommen |
| 5 | PDF erstellen | PDF wird erstellt, Erfolgsmeldung erscheint |
| 6 | PDF öffnen | QR-Code, Text, Logo und Footer werden angezeigt |
| 7 | 5-Zeilen-Layout wiederholen | PDF wird ebenfalls korrekt erstellt |

---

## Sammelverarbeitung

| Nr. | Test | Erwartetes Ergebnis |
|---:|---|---|
| 1 | Tab „Sammelverarbeitung“ öffnen | Tab wird korrekt angezeigt |
| 2 | Excel-Datei auswählen | Pfad wird übernommen |
| 3 | PDF-Speicherort auswählen | Pfad wird übernommen |
| 4 | 4-Zeilen-Layout auswählen | Layoutauswahl wird übernommen |
| 5 | PDF erstellen | Sammel-PDF wird erstellt, Erfolgsmeldung erscheint |
| 6 | PDF öffnen | Alle erwarteten Schilder werden angezeigt |
| 7 | 5-Zeilen-Layout wiederholen | Sammel-PDF wird ebenfalls korrekt erstellt |

---

## Fehlerfälle

| Nr. | Test | Erwartetes Ergebnis |
|---:|---|---|
| 1 | PDF erstellen ohne Eingabe | Button bleibt deaktiviert oder Erstellung wird verhindert |
| 2 | PDF erstellen ohne Speicherpfad | Button bleibt deaktiviert oder Erstellung wird verhindert |
| 3 | Sammelverarbeitung ohne Excel-Datei | Button bleibt deaktiviert oder Erstellung wird verhindert |
| 4 | Sammelverarbeitung mit ungültiger Excel-Datei | Verständliche Fehlermeldung erscheint |
| 5 | PDF-Datei während der Erstellung geöffnet lassen | Fehler wird sauber abgefangen oder verständlich gemeldet |

---

## Abschlussprüfung vor Commit

Vor jedem Commit sollten mindestens diese Punkte geprüft werden:

```powershell
python main.py
```

Danach manuell prüfen:

* Programm startet
* Einzelerstellung funktioniert
* Sammelverarbeitung funktioniert
* Handbuch öffnet
* Release Notes öffnen
* Keine Fehlermeldung im Terminal

