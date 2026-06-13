# SETUP UND FEHLERBEHEBUNG

## Zweck

Dieses Dokument beschreibt die empfohlene lokale Einrichtung des Projekts und typische Lösungen bei Problemen mit der Python-Umgebung.

---

## Virtuelle Umgebung erstellen

Im Projektordner ausführen:

```powershell
python -m venv env
```

Danach aktivieren:

```powershell
.\env\Scripts\activate
```

Wenn die Umgebung aktiv ist, steht am Anfang der PowerShell-Zeile normalerweise:

```text
(env)
```

---

## Abhängigkeiten installieren

Empfohlen:

```powershell
pip install -r requirements.txt
```

Alternativ manuell:

```powershell
pip install openpyxl qrcode reportlab pillow
```

---

## Programm starten

```powershell
python main.py
```

---

## Pillow-/PIL-Fehler beheben

Typischer Fehler:

```text
ImportError: cannot import name '_imaging' from 'PIL'
```

Ursache:

Die Pillow-Installation in der virtuellen Umgebung ist beschädigt oder unvollständig.

Lösung:

```powershell
pip uninstall pillow
pip install --no-cache-dir pillow
```

Falls der Fehler weiterhin besteht:

```powershell
pip uninstall pillow
pip uninstall PIL
pip install --upgrade pip
pip install --no-cache-dir pillow
```

Danach erneut starten:

```powershell
python main.py
```

---

## Umgebung komplett neu aufbauen

Wenn die virtuelle Umgebung stark beschädigt ist, kann sie neu erstellt werden.

PowerShell im Projektordner:

```powershell
rmdir /s env
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
python main.py
```

---

## Wichtiger Hinweis zu Git

Die virtuelle Umgebung darf nicht nach GitHub hochgeladen werden.

Diese Ordner bleiben lokal:

```text
env/
.venv/
venv/
__pycache__/
output/
```

Diese Einträge sind in `.gitignore` vorgesehen.

