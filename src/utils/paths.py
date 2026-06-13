from pathlib import Path
import sys


def project_root() -> Path:
    """Gibt den Projektwurzelordner zurück.

    Die Berechnung ist unabhängig vom aktuellen Arbeitsverzeichnis. Dadurch
    funktionieren Assets und Beispiel-/Ausgabepfade auch dann, wenn das Programm
    aus VS Code oder über einen absoluten Pfad gestartet wird.
    """
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)

    # src/utils/paths.py -> src/utils -> src -> Projektwurzel
    return Path(__file__).resolve().parents[2]


def resource_path(relative_path: str) -> str:
    """Gibt einen absoluten Pfad zu einer Projektressource zurück."""
    return str(project_root() / relative_path)


def project_path(relative_path: str) -> Path:
    """Gibt einen pathlib-Pfad relativ zur Projektwurzel zurück."""
    return project_root() / relative_path
