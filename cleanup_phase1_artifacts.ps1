# Phase 1 Cleanup – Schildgenerator
# Zweck: Technische Artefakte aus dem lokalen Projekt entfernen.
# Hinweis: Die virtuelle Umgebung wird NICHT gelöscht, damit dein lokales Setup erhalten bleibt.

Write-Host "Starte Phase-1-Bereinigung..." -ForegroundColor Cyan

# Fehlhafte/alte Doppelstruktur entfernen, falls vorhanden
if (Test-Path "src\src") {
    Remove-Item -Recurse -Force "src\src"
    Write-Host "Entfernt: src\src"
}

# Python Cache entfernen
Get-ChildItem -Recurse -Directory -Filter "__pycache__" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
Get-ChildItem -Recurse -File -Include "*.pyc","*.pyo","*.pyd" -ErrorAction SilentlyContinue | Remove-Item -Force
Write-Host "Entfernt: Python-Cache-Dateien"

# Generierte Ausgaben optional entfernen
if (Test-Path "output") {
    Remove-Item -Recurse -Force "output"
    Write-Host "Entfernt: output"
}

# Abschlussprüfung
Write-Host "Bereinigung abgeschlossen." -ForegroundColor Green
Write-Host "Bitte jetzt ausführen: git status" -ForegroundColor Yellow
