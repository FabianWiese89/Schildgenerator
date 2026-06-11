import tkinter as tk
import webbrowser

from src.config.theme import BG_COLOR

class HandbuchWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Handbuch – Lagerplatz-QRCode-Generator")
        self.geometry("690x600")
        self.resizable(True, True)
        self.focus_set()
        self.grab_set()

        toc_items = [
            ("1. Übersicht", "uebersicht"),
            ("2. Einzelerstellung – Schritt für Schritt", "einzelerstellung"),
            ("3. Sammelverarbeitung – Schritt für Schritt", "sammelverarbeitung"),
            ("4. Zeilenanzahl – Warum ist das wichtig?", "zeilenanzahl"),
            ("5. Häufige Fehler & Lösungen", "fehler"),
            ("6. Support & Kontakt", "support"),
        ]
        self.text = tk.Text(self, wrap="word", font=("Arial", 11), padx=10, pady=10, bg=BG_COLOR, fg="black")
        self.text.pack(fill="both", expand=True, side="left")
        sb = tk.Scrollbar(self, command=self.text.yview)
        sb.pack(side="right", fill="y")
        self.text.configure(yscrollcommand=sb.set)
        self.tag_indices = {}

        self.text.insert("end", "Inhaltsverzeichnis\n", "h1")
        for idx, (label, anchor) in enumerate(toc_items, start=1):
            pos = self.text.index("end")
            self.text.insert("end", f"{label}\n", f"toc_{anchor}")
            self.text.tag_add(f"toc_{anchor}", pos, f"{pos} lineend")
            self.text.tag_bind(f"toc_{anchor}", "<Button-1>", lambda e, a=anchor: self.scroll_to(a))
            self.text.tag_config(f"toc_{anchor}", foreground="blue", underline=True, font=("Arial", 11, "bold"))
        self.text.insert("end", "\n")
        self.mark_section("uebersicht")
        self.text.insert("end", "Der Lagerplatz-QRCode-Generator ist eine Anwendung zur schnellen Erstellung von Lagerplatzschildern mit QR-Code und Firmenlogo. Sie können einzelne Schilder oder ganze Serien aus Excel-Listen erzeugen. Die fertigen Etiketten werden als PDF ausgegeben und können gedruckt oder weiterverarbeitet werden.\n\n")
        self.mark_section("einzelerstellung")
        self.text.insert("end", "2. Einzelerstellung – Schritt für Schritt\n", "h2")
        self.text.insert("end", 
            "• Tab 'Einzelerstellung' ist beim Start automatisch aktiv.\n"
            "• Wählen Sie zunächst die gewünschte Zeilenanzahl (4 oder 5 Zeilen).\n"
            "• Geben Sie den Lagerplatz im systemischen Format (mit Bindestrichen, z. B. 05-H2-11-093-L) ein.\n"
            "• Wählen Sie einen Speicherort für die PDF-Datei aus.\n"
            "• Klicken Sie auf 'PDF erstellen'.\n"
            "Das Programm generiert automatisch die visuelle Darstellung ohne Bindestriche und den passenden QR-Code. Das PDF enthält Ihr Firmenlogo, den Lagerplatztext und den Hinweis in der Fußzeile.\n\n"
            "Tipp: Die Auswahl der richtigen Zeilenanzahl ist entscheidend, siehe dazu auch Abschnitt 4.\n\n"
        )
        self.mark_section("sammelverarbeitung")
        self.text.insert("end", "3. Sammelverarbeitung – Schritt für Schritt\n", "h2")
        self.text.insert("end", 
            "• Wechseln Sie in den Tab 'Sammelverarbeitung'.\n"
            "• Wählen Sie die gewünschte Zeilenanzahl (4 oder 5 Zeilen).\n"
            "• Wählen Sie eine Excel-Datei im .xlsx-Format ohne Überschrift aus.\n"
            "     - Spalte A: Lagerplatztext mit Leerzeichen (visuelle Darstellung)\n"
            "     - Spalte B: Lagerplatz im systemischen Format (mit Bindestrichen)\n"
            "• Wählen Sie den Speicherort für das kombinierte PDF.\n"
            "• Klicken Sie auf 'PDF erstellen'.\n"
            "Für jede Zeile in der Excel wird eine Seite im PDF generiert, das PDF enthält das Firmenlogo, den QR-Code, den Lagerplatztext und den Hinweis in der Fußzeile.\n\n"
            "Tipp: Die Formatierung der Excel-Datei ist entscheidend für ein korrektes Ergebnis. Siehe Hinweise in der Maske.\n\n"
        )
        self.mark_section("zeilenanzahl")
        self.text.insert("end", "4. Zeilenanzahl – Warum ist das wichtig?\n", "h2")
        self.text.insert("end",
            "Die Auswahl der Zeilenanzahl bestimmt, wie der Text auf dem PDF angeordnet und formatiert wird. "
            "Achten Sie unbedingt darauf, die Zeilenanzahl entsprechend der tatsächlichen Anzahl an Zeilen im Etikett auszuwählen!\n\n"
            "• Wählen Sie 5 Zeilen pro Seite, aber Ihr Text besteht nur aus 4 Zeilen:\n"
            "     → Das Ergebnis ist möglicherweise falsch formatiert, es entsteht viel Weißraum oder der Text sitzt nicht optimal.\n"
            "• Wählen Sie 4 Zeilen, obwohl Ihr Text 5 Zeilen hat:\n"
            "     → Die letzte Zeile kann abgeschnitten oder zu klein dargestellt werden.\n"
            "• Folgen:\n"
            "     - Die Etiketten sind nicht korrekt lesbar.\n"
            "     - Informationen können fehlen oder unleserlich sein.\n\n"
            "Prüfen Sie vor der Erstellung, wie viele Zeilen Ihr Text hat und wählen Sie entsprechend aus, damit das fertige PDF optimal aufgebaut wird.\n\n"
        )
        self.mark_section("fehler")
        self.text.insert("end", "5. Häufige Fehler & Lösungen\n", "h2")
        self.text.insert("end",
            "• Die Excel-Datei enthält eine Überschrift:\n"
            "     → Entfernen Sie alle Überschriften, die erste Zeile muss bereits Daten enthalten.\n"
            "• Spalte B ist leer oder falsch formatiert:\n"
            "     → Prüfen Sie, dass in Spalte B der Lagerplatz mit Bindestrichen steht.\n"
            "• Das Firmenlogo wird nicht angezeigt:\n"
            "     → Stellen Sie sicher, dass die Bilddatei 'IMG_0060.jpeg' im Programmordner liegt.\n"
            "• PDF kann nicht gespeichert werden:\n"
            "     → Prüfen Sie die Zugriffsrechte und dass das Zielverzeichnis existiert.\n"
            "• Keine Ausgabe, Button bleibt grau:\n"
            "     → Kontrollieren Sie die Eingaben und Dateiauswahl. Alle Felder müssen korrekt ausgefüllt sein.\n\n"
        )
        self.mark_section("support")
        self.text.insert("end", "6. Support & Kontakt\n", "h2")
        self.text.insert("end", 
            "Bei Fragen, Problemen oder Verbesserungsvorschlägen nutzen Sie bitte die Support-Funktion in der App. "
            "Sie erreichen mich direkt per E-Mail:\n"
        )
        start = self.text.index("end")
        self.text.insert("end", "fabian.wiese@schnellecke.com\n", "emaillink")
        end = self.text.index("end")
        self.text.tag_add("emaillink", start, end)
        self.text.tag_config("emaillink", foreground="blue", underline=True)
        self.text.tag_bind("emaillink", "<Button-1>", lambda e: webbrowser.open("mailto:fabian.wiese@schnellecke.com"))
        self.text.insert("end", "\n")
        self.text.tag_config("h1", font=("Arial", 13, "bold"))
        self.text.tag_config("h2", font=("Arial", 12, "bold"), spacing1=8, spacing3=4)
        self.text.config(state="disabled")

    def mark_section(self, anchor):
        pos = self.text.index("end")
        self.text.insert("end", "\n")
        self.text.mark_set(anchor, pos)

    def scroll_to(self, anchor):
        self.text.see(anchor)
        self.text.tag_remove("sel", "1.0", "end")
        self.text.tag_add("sel", anchor, f"{anchor} lineend")

# Hauptklasse des Programms
