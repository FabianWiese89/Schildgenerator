import os

def is_single_pdf_valid(lagerplatz, pdf, layout):
    return (
        layout in ["4 Zeilen pro PDF-Seite", "5 Zeilen pro PDF-Seite"]
        and len(lagerplatz) >= 7
        and "-" in lagerplatz
        and pdf.endswith(".pdf")
    )
    
def is_batch_pdf_valid(excel, pdf, layout):
    return (
        layout in ["4 Zeilen pro PDF-Seite", "5 Zeilen pro PDF-Seite"]
        and excel.endswith(".xlsx")
        and pdf.endswith(".pdf")
        and os.path.exists(excel)
    )