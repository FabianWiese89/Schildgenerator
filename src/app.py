import os
import tkinter as tk

from PIL import Image, ImageTk
from tkinter import filedialog, messagebox, ttk
from src.gui import ReleaseNotesWindow, HandbuchWindow
from src.services import open_support_email

from src.utils import (
    get_line_count_from_layout,
    resource_path,
    is_single_pdf_valid,
    is_batch_pdf_valid,
)

from src.pdf import (
    generate_pdf_einzeln,
    generate_text_sign_pdf,
    generate_batch_pdf_4,
    generate_batch_pdf_5,
)
from src.config import (
    BG_COLOR,
    BUTTON_COLOR,
    GUI_LOGO_PATH,
    GUI_LOGO_WIDTH,
    GUI_LOGO_HEIGHT,
    GUI_LOGO_RELX,
    GUI_LOGO_RELY,
    GUI_LOGO_ANCHOR,
)
# ---- Farbdefinitionen ----
class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lagerplatz-QRCode-Generator Version 1.0")
        self.root.geometry("810x600")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        # Tabs
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook.Tab', background=BG_COLOR, font=('Arial', 11, 'bold'), padding=[16, 6])
        style.map('TNotebook.Tab', background=[('selected', '#bdbdbd')])

        self.notebook = ttk.Notebook(root)
        self.tab_single = tk.Frame(self.notebook, bg=BG_COLOR)
        self.tab_batch = tk.Frame(self.notebook, bg=BG_COLOR)
        self.notebook.add(self.tab_single, text="Einzelerstellung")
        self.notebook.add(self.tab_batch, text="Sammelverarbeitung")
        self.notebook.pack(fill="both", expand=True, padx=40, pady=28)

        # Trennstrich unter den Tabs
        separator = tk.Frame(root, bg="#6e6e6e", height=2)
        separator.pack(fill="x", padx=30, pady=(0, 8))

        self.notebook.select(0)  # Einzelerstellung ist Standard

        # Einzel-TAB Variablen
        self.single_lagerplatz = tk.StringVar()
        self.single_layout = tk.StringVar(value="Bitte wählen...")
        self.single_output = tk.StringVar()
        self.single_status = None
        self.single_btn_pdf = None

        # Batch-TAB Variablen
        self.batch_excel_path = tk.StringVar()
        self.batch_layout = tk.StringVar(value="Bitte wählen...")
        self.batch_output_path = tk.StringVar()
        self.batch_status = None
        self.batch_btn_pdf = None

        self.build_tab_single()
        self.build_tab_batch()
        self.build_version_label()

    # ==== VERSION LABEL MIT RELEASE NOTES ====
    def build_version_label(self):
        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.place(relx=0, rely=1.0, anchor="sw", x=12, y=-8)

        self.version_lbl = tk.Label(
            frame,
            text="© Fabian Wiese – Version 1.0 ⓘ",
            fg="black",
            bg=BG_COLOR,
            cursor="arrow"
        )
        self.version_lbl.pack(anchor="sw")
        self.version_lbl.bind("<Enter>", self._on_version_hover)
        self.version_lbl.bind("<Leave>", self._on_version_leave)
        self.version_lbl.bind("<Button-1>", self.show_release_notes)

    def add_logo_to_frame(self, frame):
        logo_path = resource_path(GUI_LOGO_PATH)

        if os.path.exists(logo_path):
            img = Image.open(logo_path)
            img = img.resize((GUI_LOGO_WIDTH, GUI_LOGO_HEIGHT), Image.LANCZOS)
            logo_img = ImageTk.PhotoImage(img)

            logo_label = tk.Label(frame, image=logo_img, bg=BG_COLOR)
            logo_label.image = logo_img
            logo_label.place(
                relx=GUI_LOGO_RELX,
                rely=GUI_LOGO_RELY,
                anchor=GUI_LOGO_ANCHOR,
            )
        
    def _on_version_hover(self, event):
        self.version_lbl.config(fg="white", font=("Arial", 10, "underline"), cursor="hand2")

    def _on_version_leave(self, event):
        self.version_lbl.config(fg="black", font=("Arial", 10, "normal"), cursor="arrow")

    def show_release_notes(self, event=None):
        ReleaseNotesWindow(self.root)

    # ==== EINZELERSTELLUNG ====
    def build_tab_single(self):
        frame = self.tab_single

        # Firmenlogo
        self.add_logo_to_frame(frame)
        
        # Titel
        tk.Label(
            frame,
            text="Ein einzelnes Lagerplatzschild generieren",
            font=("Arial", 12, "bold"),
            bg=BG_COLOR
        ).grid(row=0, column=0, sticky="w", pady=(10, 8), columnspan=2)

        # Layout Dropdown
        tk.Label(
            frame,
            text="Wie viele Zeilen Text soll dein Lagerplatzetikett enthalten?",
            font=("Arial", 10),
            bg=BG_COLOR
        ).grid(row=1, column=0, sticky="w", padx=(0,0))
        layout_dropdown = ttk.Combobox(
            frame,
            textvariable=self.single_layout,
            values=["Bitte wählen...", "4 Zeilen pro PDF-Seite", "5 Zeilen pro PDF-Seite"],
            state="readonly",
            width=30
        )
        layout_dropdown.grid(row=2, column=0, sticky="w", pady=(0, 10))
        layout_dropdown.bind("<<ComboboxSelected>>", lambda e: self.update_single_button())

        # Eingabe Lagerplatz (systemisch)
        tk.Label(
            frame,
            text="Lagerplatz (systemisch, mit Bindestrichen):",
            font=("Arial", 10),
            bg=BG_COLOR
        ).grid(row=3, column=0, sticky="w", pady=(0, 2))
        tk.Entry(frame, textvariable=self.single_lagerplatz, width=50, bg=BG_COLOR, fg="black", insertbackground="black").grid(row=4, column=0, sticky="w")

        # Speicherort Auswahl
        tk.Label(
            frame,
            text="Speicherort für das PDF:",
            font=("Arial", 10),
            bg=BG_COLOR
        ).grid(row=5, column=0, pady=(14, 0), sticky="w")
        tk.Entry(frame, textvariable=self.single_output, width=60, bg=BG_COLOR, fg="black", insertbackground="black").grid(row=6, column=0, sticky="w")
        tk.Button(frame, text="Durchsuchen", command=self.single_save_pdf, bg=BUTTON_COLOR, fg="black").grid(row=6, column=1, padx=10)

        # Status-Label
        self.single_status = tk.Label(frame, text="Bereit", fg="blue", bg=BG_COLOR)
        self.single_status.grid(row=7, column=0, pady=(15, 0), sticky="w")

        # Buttons
        btn_frame = tk.Frame(frame, bg=BG_COLOR)
        btn_frame.grid(row=8, column=0, columnspan=2, pady=20, sticky="w")

        self.single_btn_pdf = tk.Button(
            btn_frame,
            text="PDF erstellen",
            command=self.on_single_generate,
            bg=BUTTON_COLOR,
            fg="black",
            padx=20,
            pady=5,
            state="disabled"
        )
        self.single_btn_pdf.pack(side="left", padx=(0, 20))

        tk.Button(
            btn_frame,
            text="Kontakt / Support",
            command=self.open_email,
            bg=BUTTON_COLOR,
            fg="black",
            padx=18,
            pady=5
        ).pack(side="left")

        # Handbuch-Button unten rechts
        tk.Button(
            frame,
            text="Handbuch",
            command=self.show_handbuch,
            bg=BUTTON_COLOR,
            fg="black",
            relief="raised"
        ).place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        
        tk.Button(
            btn_frame,
            text="Textschild Test",
            command=lambda: generate_text_sign_pdf(
                "TESTSCHILD",
                "PARKPLATZ FÜR BESUCHER UND LIEFERANTEN SOWIE EXTERNE DIENSTLEISTER",
                "output/test_textschild.pdf",
                True
            ),
            bg=BUTTON_COLOR,
            fg="black",
            padx=18,
            pady=5
        ).pack(side="left", padx=(0, 20))

        # Live-Validation
        frame.bind_all('<KeyRelease>', lambda e: self.update_single_button())
        frame.bind_all('<<ComboboxSelected>>', lambda e: self.update_single_button())

    def show_handbuch(self):
        HandbuchWindow(self.root)

    def update_single_button(self):
        lagerplatz = self.single_lagerplatz.get().strip()
        pdf = self.single_output.get().strip()
        layout = self.single_layout.get()
        if is_single_pdf_valid(lagerplatz, pdf, layout):
            self.single_btn_pdf.config(state="normal")
        else:
            self.single_btn_pdf.config(state="disabled")

    def single_save_pdf(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF-Dateien", "*.pdf")]
        )
        if path:
            self.single_output.set(path)
            self.update_single_button()

    def on_single_generate(self):
        self.single_status.config(text="PDF wird erstellt...")
        self.root.update_idletasks()
        choice = get_line_count_from_layout(self.single_layout.get())
        lagerplatz_sys = self.single_lagerplatz.get().strip()
        lagerplatz_vis = lagerplatz_sys.replace("-", " ")
        qr_data = lagerplatz_sys

        output = self.single_output.get().strip()
        if choice == 4:
            generate_pdf_einzeln(lagerplatz_vis, qr_data, output, 4)
        else:
            generate_pdf_einzeln(lagerplatz_vis, qr_data, output, 5)
        self.single_status.config(text="Fertig")
        messagebox.showinfo("Fertig", f"PDF erfolgreich erstellt:\n{output}")

    # ==== SAMMELVERARBEITUNG ====
    def build_tab_batch(self):
        frame = self.tab_batch

        # Firmenlogo
        self.add_logo_to_frame(frame)

        # Titel
        tk.Label(
            frame,
            text="Lagerplatz-Schilder aus Excel-Datei generieren.",
            font=("Arial", 12, "bold"),
            bg=BG_COLOR
        ).grid(row=0, column=0, sticky="w", pady=(10, 8), columnspan=2)

        # Layout Dropdown
        tk.Label(
            frame,
            text="Wie viele Zeilen Text soll dein Lagerplatzetikett enthalten?",
            font=("Arial", 10),
            bg=BG_COLOR
        ).grid(row=1, column=0, sticky="w", padx=(0,0))
        layout_dropdown = ttk.Combobox(
            frame,
            textvariable=self.batch_layout,
            values=["Bitte wählen...", "4 Zeilen pro PDF-Seite", "5 Zeilen pro PDF-Seite"],
            state="readonly",
            width=30
        )
        layout_dropdown.grid(row=2, column=0, sticky="w", pady=(0, 14))
        layout_dropdown.bind("<<ComboboxSelected>>", lambda e: self.update_batch_button())

        # Excel-Dateiauswahl
        tk.Label(frame, text="Excel-Datei auswählen:", bg=BG_COLOR).grid(row=3, column=0, sticky="w")
        tk.Entry(frame, textvariable=self.batch_excel_path, width=60, bg=BG_COLOR, fg="black", insertbackground="black").grid(row=4, column=0, sticky="w")
        tk.Button(frame, text="Durchsuchen", command=self.browse_batch_excel, bg=BUTTON_COLOR, fg="black").grid(row=4, column=1, padx=10)

        # Hinweistext
        tk.Label(
            frame, text="• Es muss eine .xlsx-Datei ohne Überschrift verwendet werden.", font=("Arial", 9), fg="darkblue", bg=BG_COLOR
        ).grid(row=5, column=0, sticky="w", pady=(12, 0))
        tk.Label(
            frame, text="• Spalte A: Lagerplatz mit Leerzeichen (z. B. 05 H2 11 093 L)", font=("Arial", 9), fg="darkblue", bg=BG_COLOR
        ).grid(row=6, column=0, sticky="w")
        tk.Label(
            frame, text="• Spalte B: Lagerplatz mit Bindestrichen (z. B. 05-H2-11-093-L)", font=("Arial", 9), fg="darkblue", bg=BG_COLOR
        ).grid(row=7, column=0, sticky="w")

        # Speicherort Auswahl
        tk.Label(frame, text="Speicherort für die kombinierte PDF:", bg=BG_COLOR).grid(row=8, column=0, pady=(16, 0), sticky="w")
        tk.Entry(frame, textvariable=self.batch_output_path, width=60, bg=BG_COLOR, fg="black", insertbackground="black").grid(row=9, column=0, sticky="w")
        tk.Button(frame, text="Durchsuchen", command=self.save_batch_pdf, bg=BUTTON_COLOR, fg="black").grid(row=9, column=1, padx=10)

        # Status-Label
        self.batch_status = tk.Label(frame, text="Bereit", fg="blue", bg=BG_COLOR)
        self.batch_status.grid(row=10, column=0, pady=(15, 0), sticky="w")

        # Buttons
        btn_frame = tk.Frame(frame, bg=BG_COLOR)
        btn_frame.grid(row=11, column=0, columnspan=2, pady=20, sticky="w")

        self.batch_btn_pdf = tk.Button(
            btn_frame,
            text="PDF erstellen",
            command=self.on_batch_generate,
            bg=BUTTON_COLOR,
            fg="black",
            padx=20,
            pady=5,
            state="disabled"
        )
        self.batch_btn_pdf.pack(side="left", padx=(0, 20))

        tk.Button(
            btn_frame,
            text="Kontakt / Support",
            command=self.open_email,
            bg=BUTTON_COLOR,
            fg="black",
            padx=18,
            pady=5
        ).pack(side="left")

        # Handbuch-Button unten rechts
        tk.Button(
            frame,
            text="Handbuch",
            command=self.show_handbuch,
            bg=BUTTON_COLOR,
            fg="black",
            relief="raised"
        ).place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        # Live-Validation
        frame.bind_all('<KeyRelease>', lambda e: self.update_batch_button())
        frame.bind_all('<<ComboboxSelected>>', lambda e: self.update_batch_button())

    def update_batch_button(self):
        excel = self.batch_excel_path.get().strip()
        pdf = self.batch_output_path.get().strip()
        zeilen = self.batch_layout.get()
        if is_batch_pdf_valid(excel, pdf, zeilen):
            self.batch_btn_pdf.config(state="normal")
        else:
            self.batch_btn_pdf.config(state="disabled")

    def browse_batch_excel(self):
        path = filedialog.askopenfilename(
            title="Excel-Datei wählen",
            filetypes=[("Excel-Dateien", "*.xlsx")]
        )
        if path:
            self.batch_excel_path.set(path)
            self.update_batch_button()

    def save_batch_pdf(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF-Dateien", "*.pdf")]
        )
        if path:
            self.batch_output_path.set(path)
            self.update_batch_button()

    def on_batch_generate(self):
        self.batch_status.config(text="PDF wird erstellt...")
        self.root.update_idletasks()
        choice = get_line_count_from_layout(self.batch_layout.get())
        excel = self.batch_excel_path.get()
        output = self.batch_output_path.get()
        if choice == 4:
            generate_batch_pdf_4(excel, output)
        else:
            generate_batch_pdf_5(excel, output)
        self.batch_status.config(text="Fertig")
        messagebox.showinfo("Fertig", f"PDF erfolgreich erstellt:\n{self.batch_output_path.get()}")

    def open_email(self):
        open_support_email()
    
    # ==== BATCH GENERIERUNG (wie bisher) ====
    
def main():
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()