import os

from src.config import VALID_LAYOUT_OPTIONS

def is_single_pdf_valid(lagerplatz, pdf, layout):
    return (
        layout in VALID_LAYOUT_OPTIONS
        and len(lagerplatz) >= 7
        and "-" in lagerplatz
        and pdf.endswith(".pdf")
    )
    
def is_batch_pdf_valid(excel, pdf, layout):
    return (
        layout in VALID_LAYOUT_OPTIONS
        and excel.endswith(".xlsx")
        and pdf.endswith(".pdf")
        and os.path.exists(excel)
    )