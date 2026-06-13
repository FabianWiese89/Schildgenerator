from pathlib import Path

from src.config import VALID_LAYOUT_OPTIONS


def has_pdf_extension(path: str) -> bool:
    return Path(str(path).strip()).suffix.lower() == ".pdf"


def has_excel_extension(path: str) -> bool:
    return Path(str(path).strip()).suffix.lower() == ".xlsx"


def is_single_pdf_valid(lagerplatz, pdf, layout):
    lagerplatz = str(lagerplatz).strip()
    pdf = str(pdf).strip()

    return (
        layout in VALID_LAYOUT_OPTIONS
        and len(lagerplatz) >= 7
        and "-" in lagerplatz
        and has_pdf_extension(pdf)
    )


def is_batch_pdf_valid(excel, pdf, layout):
    excel_path = Path(str(excel).strip())
    pdf = str(pdf).strip()

    return (
        layout in VALID_LAYOUT_OPTIONS
        and has_excel_extension(str(excel_path))
        and excel_path.exists()
        and excel_path.is_file()
        and has_pdf_extension(pdf)
    )
