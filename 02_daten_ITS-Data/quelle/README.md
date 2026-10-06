# quelle – lokaler Spiegel der Azure-Quelle `mabeehavenraw/source-data`

Neue Rohdaten-Lieferungen, bevor die Pipeline sie nach Bronze kopiert. Dateinamen `<sensor>_<stadt>.csv`.

- `*_wurzburg.csv` (4 Sensoren): Kaggle „Beehive Metrics“ (HOBOS, https://www.hobos.de), heruntergeladen 30.09.2026 für den Test mit einer zweiten Stadt. **Lizenz unbekannt → nicht veröffentlichen** (CSV sind per `.gitignore` ausgeschlossen).
- Befunde (Abweichungen zu Schwartau): Gewicht in kg und minütlich, Feuchte stündlich, Temperatur mit Fehlerwerten bis −227 °C, flow nicht sauber in zwei Reihen, Lücke Mai–Okt. 2018 – siehe Übergabe/Pflichtenheft.
- **01.10.2026:** Kursfassung (WBS, `data_2022.zip`, „New Data Drop“) übernommen. humidity/weight/temperature identisch mit Kaggle; **flow abweichend: in der Kursfassung fehlt ab 02.01.2019 täglich die Stunde 00:00–00:59** (8.100 Minuten). Kaggle-flow im `_archiv` (`flow_wurzburg__kaggle_bis_<UTC>.csv`). Entscheidung Projektleitung: Kursfassung verwenden.
