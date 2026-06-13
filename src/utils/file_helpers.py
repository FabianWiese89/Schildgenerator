from pathlib import Path


def ensure_pdf_output_path(output_path: str) -> Path:
    """Prüft und normalisiert einen PDF-Ausgabepfad."""
    if not output_path or not str(output_path).strip():
        raise ValueError("Bitte einen Speicherort für die PDF-Datei auswählen.")

    path = Path(str(output_path).strip()).expanduser()

    if path.suffix.lower() != ".pdf":
        raise ValueError("Der Speicherort muss auf eine PDF-Datei enden (.pdf).")

    if path.exists() and path.is_dir():
        raise ValueError("Der gewählte PDF-Speicherort ist ein Ordner. Bitte eine PDF-Datei auswählen.")

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise OSError(
            "Der Zielordner für die PDF-Datei konnte nicht erstellt oder geöffnet werden. "
            "Bitte prüfe den Speicherort und deine Schreibrechte."
        ) from exc

    return path


def ensure_excel_input_path(excel_path: str) -> Path:
    """Prüft, ob eine vorhandene Excel-Datei für die Sammelverarbeitung gewählt wurde."""
    if not excel_path or not str(excel_path).strip():
        raise ValueError("Bitte eine Excel-Datei auswählen.")

    path = Path(str(excel_path).strip()).expanduser()

    if path.suffix.lower() != ".xlsx":
        raise ValueError("Bitte eine Excel-Datei im Format .xlsx auswählen.")

    if not path.exists():
        raise FileNotFoundError("Die ausgewählte Excel-Datei wurde nicht gefunden.")

    if not path.is_file():
        raise ValueError("Der gewählte Excel-Pfad ist keine Datei.")

    if path.name.startswith("~$"):
        raise ValueError(
            "Die ausgewählte Excel-Datei sieht wie eine temporäre Office-Datei aus. "
            "Bitte die normale .xlsx-Datei auswählen und Excel ggf. schließen."
        )

    return path


def ensure_required_file(path: str, description: str) -> Path:
    """Prüft, ob eine benötigte Projektdatei vorhanden ist."""
    file_path = Path(path)

    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError(
            f"{description} wurde nicht gefunden: {file_path}\n"
            "Bitte prüfe, ob der Projektordner vollständig ist."
        )

    return file_path
