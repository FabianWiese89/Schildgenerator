import os
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from src.utils import resource_path

from src.config import (
    BG_COLOR,
    BUTTON_COLOR,
    BUTTON_TEXT_COLOR,
    ENTRY_TEXT_COLOR,
    ENTRY_CURSOR_COLOR,
    GUI_LOGO_PATH,
    GUI_LOGO_WIDTH,
    GUI_LOGO_HEIGHT,
    GUI_LOGO_RELX,
    GUI_LOGO_RELY,
    GUI_LOGO_ANCHOR,
    LAYOUT_OPTIONS,
    STATUS_TEXT_COLOR,
    BUTTON_BROWSE_TEXT,
    BUTTON_CREATE_PDF_TEXT,
    BUTTON_SUPPORT_TEXT,
    BUTTON_MANUAL_TEXT,
    STATUS_READY_TEXT,
)


def add_logo_to_frame(app, frame):
    """Fügt das konfigurierte Firmenlogo in einen GUI-Frame ein."""
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


def add_handbook_button(app, frame):
    """Fügt den Handbuch-Button unten rechts in einen Tab ein."""
    tk.Button(
        frame,
        text=BUTTON_MANUAL_TEXT,
        command=app.show_handbuch,
        bg=BUTTON_COLOR,
        fg=BUTTON_TEXT_COLOR,
        relief="raised"
    ).place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)


def add_support_button(app, frame):
    """Fügt den Kontakt-/Support-Button in eine Buttonleiste ein."""
    tk.Button(
        frame,
        text=BUTTON_SUPPORT_TEXT,
        command=app.open_email,
        bg=BUTTON_COLOR,
        fg=BUTTON_TEXT_COLOR,
        padx=18,
        pady=5
    ).pack(side="left", padx=(0, 20))


def add_browse_button(frame, command, row):
    """Fügt einen Durchsuchen-Button in einer Formularzeile ein."""
    tk.Button(
        frame,
        text=BUTTON_BROWSE_TEXT,
        command=command,
        bg=BUTTON_COLOR,
        fg=BUTTON_TEXT_COLOR
    ).grid(row=row, column=1, padx=10)


def add_layout_combobox(frame, variable, row, pady):
    """Fügt eine Layout-Combobox ein und gibt sie zurück."""
    layout_dropdown = ttk.Combobox(
        frame,
        textvariable=variable,
        values=LAYOUT_OPTIONS,
        state="readonly",
        width=30
    )
    layout_dropdown.grid(row=row, column=0, sticky="w", pady=pady)
    return layout_dropdown


def add_create_pdf_button(frame, command):
    """Erzeugt den deaktivierten PDF-Erstellen-Button und gibt ihn zurück."""
    return tk.Button(
        frame,
        text=BUTTON_CREATE_PDF_TEXT,
        command=command,
        bg=BUTTON_COLOR,
        fg=BUTTON_TEXT_COLOR,
        state="disabled",
        padx=20,
        pady=8
    )


def add_status_label(frame):
    """Erzeugt ein Statuslabel mit dem Standardstatus."""
    return tk.Label(
        frame,
        text=STATUS_READY_TEXT,
        fg=STATUS_TEXT_COLOR,
        bg=BG_COLOR
    )


def add_text_entry(frame, variable, row, width):
    """Fügt ein einzeiliges Texteingabefeld ein und gibt es zurück."""
    entry = tk.Entry(
        frame,
        textvariable=variable,
        width=width,
        bg=BG_COLOR,
        fg=ENTRY_TEXT_COLOR,
        insertbackground=ENTRY_CURSOR_COLOR
    )
    entry.grid(row=row, column=0, sticky="w")
    return entry
