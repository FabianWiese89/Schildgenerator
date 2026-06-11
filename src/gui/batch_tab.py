import tkinter as tk

from src.config import (
    BG_COLOR,
    FONT_TITLE,
    FONT_LABEL,
    FONT_HINT,
    HINT_TEXT_COLOR,
    BATCH_TAB_TITLE_TEXT,
    BATCH_LAYOUT_LABEL_TEXT,
    BATCH_EXCEL_LABEL_TEXT,
    BATCH_OUTPUT_LABEL_TEXT,
    BATCH_HINT_NO_HEADER_TEXT,
    BATCH_HINT_COLUMN_A_TEXT,
    BATCH_HINT_COLUMN_B_TEXT,
)


def build_batch_tab(app):
    """Erstellt den GUI-Inhalt für den Tab Sammelverarbeitung.

    Diese Datei enthält ausschließlich den Oberflächenaufbau für den Tab
    Sammelverarbeitung. Die zugehörige Steuerungslogik liegt getrennt im jeweiligen
    Actions-Modul.
    """
    frame = app.tab_batch

    # Firmenlogo
    app.add_logo_to_frame(frame)

    # Titel
    tk.Label(
        frame,
        text=BATCH_TAB_TITLE_TEXT,
        font=FONT_TITLE,
        bg=BG_COLOR
    ).grid(row=0, column=0, sticky="w", pady=(10, 8), columnspan=2)

    # Layout Dropdown
    tk.Label(
        frame,
        text=BATCH_LAYOUT_LABEL_TEXT,
        font=FONT_LABEL,
        bg=BG_COLOR
    ).grid(row=1, column=0, sticky="w", padx=(0, 0))

    layout_dropdown = app.add_layout_combobox(
        frame,
        app.batch_layout,
        row=2,
        pady=(0, 14)
    )
    layout_dropdown.bind("<<ComboboxSelected>>", lambda e: app.update_batch_button())

    # Excel-Dateiauswahl
    tk.Label(
        frame,
        text=BATCH_EXCEL_LABEL_TEXT,
        font=FONT_LABEL,
        bg=BG_COLOR
    ).grid(row=3, column=0, sticky="w")

    app.add_text_entry(frame, app.batch_excel_path, row=4, width=60)
    app.add_browse_button(frame, app.browse_batch_excel, row=4)

    # Hinweistext
    tk.Label(
        frame,
        text=BATCH_HINT_NO_HEADER_TEXT,
        font=FONT_HINT,
        fg=HINT_TEXT_COLOR,
        bg=BG_COLOR
    ).grid(row=5, column=0, sticky="w", pady=(12, 0))

    tk.Label(
        frame,
        text=BATCH_HINT_COLUMN_A_TEXT,
        font=FONT_HINT,
        fg=HINT_TEXT_COLOR,
        bg=BG_COLOR
    ).grid(row=6, column=0, sticky="w")

    tk.Label(
        frame,
        text=BATCH_HINT_COLUMN_B_TEXT,
        font=FONT_HINT,
        fg=HINT_TEXT_COLOR,
        bg=BG_COLOR
    ).grid(row=7, column=0, sticky="w")

    # Speicherort Auswahl
    tk.Label(
        frame,
        text=BATCH_OUTPUT_LABEL_TEXT,
        font=FONT_LABEL,
        bg=BG_COLOR
    ).grid(row=8, column=0, pady=(16, 0), sticky="w")

    app.add_text_entry(frame, app.batch_output_path, row=9, width=60)
    app.add_browse_button(frame, app.save_batch_pdf, row=9)

    # PDF-Erstellen-Button und Support-Button
    btn_frame = tk.Frame(frame, bg=BG_COLOR)
    btn_frame.grid(row=10, column=0, columnspan=2, pady=20, sticky="w")

    app.batch_btn_pdf = app.add_create_pdf_button(btn_frame, app.on_batch_generate)
    app.batch_btn_pdf.pack(side="left", padx=(0, 20))

    app.add_support_button(btn_frame)

    # Status-Label
    app.batch_status = app.add_status_label(frame)
    app.batch_status.grid(row=11, column=0, sticky="w")

    # Handbuch-Button unten rechts
    app.add_handbook_button(frame)

    # Live-Validation
    frame.bind_all("<KeyRelease>", lambda e: app.update_batch_button())
    frame.bind_all("<<ComboboxSelected>>", lambda e: app.update_batch_button())
