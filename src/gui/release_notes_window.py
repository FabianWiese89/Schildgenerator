import tkinter as tk

from src.config.theme import BG_COLOR

class ReleaseNotesWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Release Notes / Changelog – Lagerplatz-QRCode-Generator")
        self.geometry("600x470")
        self.resizable(True, True)
        self.focus_set()
        self.grab_set()

        txt = tk.Text(self, wrap="word", font=("Arial", 11), padx=10, pady=10, bg=BG_COLOR, fg="black")
        txt.pack(fill="both", expand=True, side="left")
        sb = tk.Scrollbar(self, command=txt.yview)
        sb.pack(side="right", fill="y")
        txt.configure(yscrollcommand=sb.set)

        changelog = (
            "Release Notes / Änderungsprotokoll\n\n"
            "Version 1.1 – 11.06.2026\n"
            "- Architektur- und Modularisierungsrelease vorbereitet\n"
            "- Projektstruktur in src/gui, src/pdf, src/config, src/utils und src/services aufgeteilt\n"
            "- Hauptfensterklasse nach src/gui/main_window.py ausgelagert und strukturell bereinigt\n"
            "- Einzelerstellung in Oberfläche und Steuerungslogik getrennt\n"
            "- Sammelverarbeitung in Oberfläche und Steuerungslogik getrennt\n"
            "- Wiederverwendbare GUI-Bausteine nach src/gui/gui_helpers.py ausgelagert\n"
            "- PDF-Erzeugung in src/pdf/generator.py gebündelt\n"
            "- Zentrale Batch-PDF-Schnittstelle generate_batch_pdf() ergänzt\n"
            "- Layout-, Theme-, Text- und Dialogwerte zentralisiert\n"
            "- Validierungs-, Pfad- und Layout-Hilfsfunktionen in src/utils ausgelagert\n"
            "- Support-Mail-Logik nach src/services ausgelagert\n"
            "- GUI-Paketimporte bereinigt und schwere Re-Exports aus src/gui/__init__.py entfernt\n"
            "- Projektstruktur-Review und Cleanup-Dokumentation ergänzt\n"
            "- Technische Artefakte über .gitignore ausgeschlossen\n"
            "- Versionsanzeige, Fenstertitel und PDF-Footer auf Version 1.1 aktualisiert\n"
            "\n"
            "Version 1.0 – 15.07.2025\n"
            "- Copyright/Version schwarz, Mouse-Over weiß\n"
            "- Tabs nun mit sichtbarem Trennstrich\n"
            "- Handbuch/Release-Notes Hintergrund grau, Text schwarz\n"
            "- Anpassung der Oberfläche in Unternehmensfarben\n"
            "- Copyright- & Versionsinfo jetzt links unten\n"
            "- Diverse kleine Usability-Verbesserungen\n"
            "- Handbuch/Bedienanleitung in der App integriert (Popup mit Navigation, Support-Link, überall erreichbar)\n"
            "- Sammelverarbeitung: Excel-Import, klare Formatvorgaben, Auswahl 4/5 Zeilen pro Schild\n"
            "- Einzelerstellung: QR-Code aus Lagerplatz-Systembezeichnung, Wahl von Zeilenzahl, PDF-Ausgabe\n"
            "- Support/Feedback-Funktion mit vorbefüllter E-Mail\n"
            "- Modernisierte Oberfläche, Logo-Einbindung, Standard-Speicherort-Auswahl\n"
            "- Benutzerführung: Tabs, Statusmeldungen, konsistente Eingabemasken\n"
            "- Release-Notes-Changelog direkt im Programm\n"
            "- Verbesserte Supportfunktion, E-Mail-Vorlage erweitert\n"
            "- GUI-Optimierungen, Logo fest integriert, konsistente Versionierung\n"
            "- Initiales Release mit Excel-zu-PDF-Funktion\n"
            "- Einzel- und Sammelverarbeitung als getrennte Skripte\n"
            "- Grundlegende Automatisierung\n"
            "\n"
            "Hinweis: Diese Übersicht wird bei neuen Updates fortgeführt.\n"
        )

        txt.insert("end", changelog)
        txt.config(state="disabled")
