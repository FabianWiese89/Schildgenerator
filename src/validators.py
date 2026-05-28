def is_single_pdf_valid(lagerplatz, pdf, layout):
    return (
        layout in ["4 Zeilen pro PDF-Seite", "5 Zeilen pro PDF-Seite"]
        and len(lagerplatz) >= 7
        and "-" in lagerplatz
        and pdf.endswith(".pdf")
    )