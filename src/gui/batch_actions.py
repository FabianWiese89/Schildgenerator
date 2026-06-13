from tkinter import filedialog, messagebox

from src.pdf import generate_batch_pdf

from src.utils import (
    get_line_count_from_layout,
    is_batch_pdf_valid,
)

from src.config import (
    STATUS_CREATING_PDF_TEXT,
    STATUS_DONE_TEXT,
    MESSAGEBOX_DONE_TITLE,
    MESSAGEBOX_PDF_CREATED_TEXT,
    PDF_DEFAULT_EXTENSION,
    PDF_FILE_TYPE_LABEL,
    PDF_FILE_PATTERN,
    EXCEL_DIALOG_TITLE,
    EXCEL_FILE_TYPE_LABEL,
    EXCEL_FILE_PATTERN,
)


def update_batch_button(app):
    """Aktualisiert den PDF-Button im Tab Sammelverarbeitung."""
    excel = app.batch_excel_path.get().strip()
    pdf = app.batch_output_path.get().strip()
    layout = app.batch_layout.get()

    if is_batch_pdf_valid(excel, pdf, layout):
        app.batch_btn_pdf.config(state="normal")
    else:
        app.batch_btn_pdf.config(state="disabled")


def browse_batch_excel(app):
    """Öffnet den Excel-Auswahldialog für die Sammelverarbeitung."""
    path = filedialog.askopenfilename(
        title=EXCEL_DIALOG_TITLE,
        filetypes=[(EXCEL_FILE_TYPE_LABEL, EXCEL_FILE_PATTERN)]
    )

    if path:
        app.batch_excel_path.set(path)
        app.update_batch_button()


def save_batch_pdf(app):
    """Öffnet den PDF-Speicherdialog für die Sammelverarbeitung."""
    path = filedialog.asksaveasfilename(
        defaultextension=PDF_DEFAULT_EXTENSION,
        filetypes=[(PDF_FILE_TYPE_LABEL, PDF_FILE_PATTERN)]
    )

    if path:
        app.batch_output_path.set(path)
        app.update_batch_button()


def on_batch_generate(app):
    """Erstellt mehrere Lagerplatzschilder aus einer Excel-Datei als PDF."""
    app.batch_status.config(text=STATUS_CREATING_PDF_TEXT)
    app.root.update_idletasks()

    choice = get_line_count_from_layout(app.batch_layout.get())
    excel = app.batch_excel_path.get()
    output = app.batch_output_path.get()

    generate_batch_pdf(excel, output, choice)

    app.batch_status.config(text=STATUS_DONE_TEXT)
    messagebox.showinfo(
        MESSAGEBOX_DONE_TITLE,
        f"{MESSAGEBOX_PDF_CREATED_TEXT}\n{output}"
    )
