"""Stadt-Fassungen der Notebooks N1–N5 automatisch erzeugen und ausführen (lokal, ohne Azure-Kosten).

Regel (Anforderung Geschäftsführung 02.10.2026): Code und Texte werden NUR in den Hauptnotebooks gepflegt
(`01_bereinigung.ipynb` … `05_analyse.ipynb`, Parameter STADT = "schwartau"). Für jede weitere Stadt aus
`lakehouse/konfiguration/standorte.csv` erzeugt dieses Skript eine Kopie in `<stadt>/`, setzt den Parameter
STADT, führt sie der Reihe nach aus (N1 → N5, jede braucht das Ergebnis der vorherigen) und speichert sie
mit Ausgaben. Grafiken landen über den Code in `04_images/<stadt>/`. Ältere Fassungen gehen ins `<stadt>/_archiv/`.

Aufruf (Umgebung „beehaven“, im Ordner 03_notebooks_ITS-Data):
    ~/miniforge3/envs/beehaven/bin/python stadt_fassungen.py wurzburg
"""
import shutil                                   # alte Fassungen ins _archiv verschieben
import sys
from datetime import datetime, timezone         # UTC-Zeitstempel für das Archiv
from pathlib import Path

import nbformat                                 # Notebooks lesen/schreiben
from nbclient import NotebookClient             # Notebooks ausführen (wie „Alle ausführen“ in VS Code)

NOTEBOOKS = ["01_bereinigung", "02_qualitaet", "03_wetter", "04_gold", "05_analyse"]   # Reihenfolge = Ausführungsreihenfolge
HAUPT_STADT = 'STADT = "schwartau"'             # Parameterzeile in den Hauptnotebooks


def fassung(name, stadt, ordner):
    """Eine Stadt-Fassung erzeugen, ausführen und speichern; gibt den Zielpfad zurück."""
    nb = nbformat.read(f"{name}.ipynb", as_version=4)
    treffer = [c for c in nb.cells if c.cell_type == "code" and HAUPT_STADT in c.source]
    if len(treffer) != 1:                       # genau eine Parameterzelle erwartet – sonst lieber abbrechen
        raise ValueError(f"{name}: Parameterzeile {HAUPT_STADT!r} nicht eindeutig gefunden ({len(treffer)}×)")
    treffer[0].source = treffer[0].source.replace(HAUPT_STADT, f'STADT = "{stadt}"')
    stempel = datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M UTC")
    kopf = nbformat.v4.new_markdown_cell(       # Hinweis oben im Notebook: nicht von Hand ändern
        f"> **{stadt.capitalize()}-Fassung** von `../{name}.ipynb`, automatisch erzeugt am {stempel} mit "
        f"`stadt_fassungen.py` (Parameter `STADT = \"{stadt}\"`, Bilder in `04_images/{stadt}/`). "
        "Code und Texte nur im Hauptnotebook ändern und neu erzeugen. Die Texte gelten für jeden Standort; "
        "die Zahlen dieser Stadt stehen in den Ausgaben, Kontrollwerte je Stadt in den Tabellen.")
    nb.cells.insert(0, kopf)
    NotebookClient(nb, timeout=1800, kernel_name="python3",
                   resources={"metadata": {"path": str(Path.cwd())}}).execute()   # im Hauptordner ausführen (gleiche relative Pfade)
    ziel = ordner / f"{name}_{stadt}.ipynb"
    if ziel.exists():                           # alte Fassung archivieren statt überschreiben
        (ordner / "_archiv").mkdir(exist_ok=True)
        utc = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
        shutil.move(ziel, ordner / "_archiv" / f"{name}_{stadt}__bis_{utc}_UTC.ipynb")
    nbformat.write(nb, ziel)
    return ziel


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    stadt = sys.argv[1]
    ordner = Path(stadt)
    ordner.mkdir(exist_ok=True)
    for name in NOTEBOOKS:
        print("ausgeführt:", fassung(name, stadt, ordner), flush=True)
