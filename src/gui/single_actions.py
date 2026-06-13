from tkinter import filedialog, messagebox

from src.pdf import generate_pdf_einzeln

from src.utils import (
    get_line_count_from_layout,
    is_single_pdf_valid,
)

from src.config import (
    ERROR_MESSAGEBOX_TITLE,
    STATUS_CREATING_PDF_TEXT,
    STATUS_DONE_TEXT,
    STATUS_ERROR_TEXT,
    MESSAGEBOX_DONE_TITLE,
    MESSAGEBOX_PDF_CREATED_TEXT,
    PDF_DEFAULT_EXTENSION,
    PDF_FILE_TYPE_LABEL,
    PDF_FILE_PATTERN,
)


def update_single_button(app):
    """Aktualisiert den PDF-Button im Tab Einzelerstellung."""
    lagerplatz = app.single_lagerplatz.get().strip()
    pdf = app.single_output.get().strip()
    layout = app.single_layout.get()

    if is_single_pdf_valid(lagerplatz, pdf, layout):
        app.single_btn_pdf.config(state="normal")
    else:
        app.single_btn_pdf.config(state="disabled")


def single_save_pdf(app):
    """Öffnet den PDF-Speicherdialog für die Einzelerstellung."""
    path = filedialog.asksaveasfilename(
        defaultextension=PDF_DEFAULT_EXTENSION,
        filetypes=[(PDF_FILE_TYPE_LABEL, PDF_FILE_PATTERN)]
    )

    if path:
        app.single_output.set(path)
        app.update_single_button()


def on_single_generate(app):
    """Erstellt ein einzelnes Lagerplatzschild als PDF."""
    app.single_status.config(text=STATUS_CREATING_PDF_TEXT)
    app.root.update_idletasks()

    try:
        choice = get_line_count_from_layout(app.single_layout.get())
        lagerplatz_sys = app.single_lagerplatz.get().strip()
        lagerplatz_vis = lagerplatz_sys.replace("-", " ")
        output = app.single_output.get().strip()

        generate_pdf_einzeln(lagerplatz_vis, lagerplatz_sys, output, choice)

        app.single_status.config(text=STATUS_DONE_TEXT)
        messagebox.showinfo(
            MESSAGEBOX_DONE_TITLE,
            f"{MESSAGEBOX_PDF_CREATED_TEXT}\n{output}"
        )
    except Exception as exc:
        app.single_status.config(text=STATUS_ERROR_TEXT)
        messagebox.showerror(ERROR_MESSAGEBOX_TITLE, str(exc))
