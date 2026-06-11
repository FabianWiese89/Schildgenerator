# Entfernt technische Python-Artefakte aus dem lokalen Projektordner.
# Die virtuelle Umgebung wird bewusst NICHT gelöscht.

if (Test-Path "src\src") {
    Remove-Item -Recurse -Force "src\src"
}

Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
Get-ChildItem -Recurse -File -Include "*.pyc","*.pyo","*.pyd" | Remove-Item -Force

Write-Host "Technische Python-Artefakte wurden bereinigt."
