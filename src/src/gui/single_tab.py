import tkinter as tk

from src.pdf import generate_text_sign_pdf

from src.config import (
    BG_COLOR,
    BUTTON_COLOR,
    BUTTON_TEXT_COLOR,
    BUTTON_TEXT_SIGN_TEST_TEXT,
    FONT_LABEL,
    FONT_TITLE,
    SHOW_TEXT_SIGN_TEST_BUTTON,
    SINGLE_LAYOUT_LABEL_TEXT,
    SINGLE_OUTPUT_LABEL_TEXT,
    SINGLE_STORAGE_LABEL_TEXT,
    SINGLE_TAB_TITLE_TEXT,
)


def build_single_tab(app):
    """Erstellt den GUI-Inhalt für den Tab Einzelerstellung.

    Die eigentliche Steuerungs- und PDF-Logik bleibt vorerst bewusst in
    QRCodeGeneratorApp. Dadurch wird nur der Oberflächenaufbau ausgelagert
    und das Risiko beim Refactoring bleibt gering.
    """
    frame = app.tab_single

    # Firmenlogo
    app.add_logo_to_frame(frame)

    # Titel
    tk.Label(
        frame,
        text=SINGLE_TAB_TITLE_TEXT,
        font=FONT_TITLE,
        bg=BG_COLOR
    ).grid(row=0, column=0, sticky="w", pady=(10, 8), columnspan=2)

    # Layout Dropdown
    tk.Label(
        frame,
        text=SINGLE_LAYOUT_LABEL_TEXT,
        font=FONT_LABEL,
        bg=BG_COLOR
    ).grid(row=1, column=0, sticky="w", padx=(0, 0))

    layout_dropdown = app.add_layout_combobox(
        frame,
        app.single_layout,
        row=2,
        pady=(0, 10)
    )
    layout_dropdown.bind("<<ComboboxSelected>>", lambda e: app.update_single_button())

    # Eingabe Lagerplatz (systemisch)
    tk.Label(
        frame,
        text=SINGLE_STORAGE_LABEL_TEXT,
        font=FONT_LABEL,
        bg=BG_COLOR
    ).grid(row=3, column=0, sticky="w", pady=(0, 2))

    app.add_text_entry(frame, app.single_lagerplatz, row=4, width=50)

    # Speicherort Auswahl
    tk.Label(
        frame,
        text=SINGLE_OUTPUT_LABEL_TEXT,
        font=FONT_LABEL,
        bg=BG_COLOR
    ).grid(row=5, column=0, pady=(14, 0), sticky="w")

    app.add_text_entry(frame, app.single_output, row=6, width=60)
    app.add_browse_button(frame, app.single_save_pdf, row=6)

    # PDF-Erstellen-Button
    app.single_btn_pdf = app.add_create_pdf_button(frame, app.on_single_generate)
    app.single_btn_pdf.grid(row=7, column=0, pady=20, sticky="w")

    # Status-Label
    app.single_status = app.add_status_label(frame)
    app.single_status.grid(row=8, column=0, sticky="w")

    # Untere Buttonleiste
    btn_frame = tk.Frame(frame, bg=BG_COLOR)
    btn_frame.grid(row=9, column=0, columnspan=2, pady=20, sticky="w")

    app.add_support_button(btn_frame)

    # Temporäre Entwicklungsfunktion:
    # Dient aktuell nur zum Testen der Textschild-PDF-Erzeugung.
    # Die spätere Vollversion soll Textschild-Inhalte über die GUI auswählbar machen.
    # Daher werden die hier verwendeten Testwerte bewusst nicht weiter zentralisiert.
    if SHOW_TEXT_SIGN_TEST_BUTTON:
        tk.Button(
            btn_frame,
            text=BUTTON_TEXT_SIGN_TEST_TEXT,
            command=lambda: generate_text_sign_pdf(
                "TESTSCHILD",
                "PARKPLATZ FÜR BESUCHER UND LIEFERANTEN SOWIE EXTERNE DIENSTLEISTER",
                "output/test_textschild.pdf",
                True
            ),
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            padx=18,
            pady=5
        ).pack(side="left", padx=(0, 20))

    # Handbuch-Button unten rechts
    app.add_handbook_button(frame)

    # Live-Validation
    frame.bind_all("<KeyRelease>", lambda e: app.update_single_button())
    frame.bind_all("<<ComboboxSelected>>", lambda e: app.update_single_button())
