# Würzburg – Notebook-Fassungen und Ergebnisse (Stand 05.10.2026)

**Was:** N1–N5 für den zweiten Standort Würzburg (HOBOS-Bienenstation Uni Würzburg). Die Notebooks werden **automatisch aus den Hauptnotebooks** in `../` erzeugt und ausgeführt: `~/miniforge3/envs/beehaven/bin/python stadt_fassungen.py wurzburg` (im Ordner `03_notebooks_ITS-Data`; `STADT = "wurzburg"`, Bilder in `04_images/wurzburg/`, alte Fassungen in `_archiv/`). Code und Texte nur in den Hauptnotebooks ändern. Die Texte gelten für jeden Standort; Kontrollwerte und Kernaussagen stehen je Stadt in Tabellen. Daten: Kursfassung „New Data Drop“ (`02_daten_ITS-Data/quelle/`, 01.01.2017–20.05.2019).

**Standortregeln** (statt fester Werte im Code): `lakehouse/konfiguration/sensoren.csv` (Einheit der Rohdaten, gültige Bereiche) und `ausschluesse.csv` (bekannte Ausfallzeiträume).

## Befunde beim ersten Lauf und Lösung

| Befund | Ursache | Lösung |
| :-- | :-- | :-- |
| Gewicht zu 100 % „ungültig“ | Würzburg liefert **kg**, Schwartau **g**; Regel rechnete in g | N1 rechnet nach `einheit_roh` einheitlich in g um; Grenze 20 kg aus der Konfiguration |
| Zeitraum E5 (Schwartau) galt auch für Würzburg | fest im Code | Ausfallzeiträume je Stadt in `ausschluesse.csv` |
| −227 °C galt als „ok“ | keine Untergrenze | gültiger Bereich −40 … 60 °C (Konfiguration) |
| N5: Honig-Auswertung H1 leer | Würzburg misst Gewicht minütlich, H1 erwartete 00:00/12:00 | Gewicht vorher auf 00:00/12:00 UTC vereinheitlicht |

Kontrolle: Schwartau liefert nach dem Umbau **identische** Ergebnisse (Gold auf das Byte gleich, N5-Kennzahlen gleich).

## Ergebnisse Würzburg im Vergleich zu Schwartau

| Kennzahl | Schwartau | Würzburg |
| :-- | :-- | :-- |
| Gewicht Median | 60 kg | 53,7 kg |
| Höchstgewicht | 91,2 kg (30.06.2017) | 68,5 kg (22.06.2017) |
| größter Verlust (vermutete Honigernte) | 32,1 kg bis 27.07.2017 | 4,6 kg bis 31.08.2017 – **keine deutliche Ernte erkennbar** (2018: Datenlücke Mai–Okt.) |
| Honig je Einflug (H1) | 6,3 mg | 7,8 mg |
| Verbrauch ohne Flug | ca. 259 g/Tag | ca. 156 g/Tag |
| Gewinnschwelle | ca. 41.500 Einflüge/Tag | ca. 20.000 Einflüge/Tag |
| Produktionstage hoch (> +0,5 kg) | 19 % | 16 % |
| Flug ↔ Außentemperatur | – | r = 0,70 |

**Deutung (vorläufig):** Würzburg ist ein **kleineres Volk** (geringeres Gewicht, weniger Verbrauch, weniger Einflüge nötig für Gewinn). Hohe Produktion an Tagen mit mehr Sonne (10,8 h) und Wärme (19 °C) – wie in Schwartau. Datenlücke Mai–Okt. 2018 (146 Tage) und fehlende Stunde 00:00–00:59 im Kurs-flow ab 2019 beachten.

## Honigproduktion im Vergleich (Notebook `../06_vergleich_standorte.ipynb`, Grafik `04_images/v1_honig_saison.png`)

Nur die Saison 2017 ist an beiden Standorten vollständig (≥ 80 % Tage mit Gewicht):

| Saison 2017 | Bad Schwartau | Würzburg |
| :-- | :-- | :-- |
| Nettozunahme in der Tracht | +41,9 kg | +19,1 kg |
| Ernte nach Höchststand | −32,1 kg (24.07.) | −4,6 kg (29.08., eher Eingriff – zu prüfen) |
| geschätzter Saisonertrag (Untergrenze) | ca. 74 kg | ca. 24 kg |
| Einflüge in der Saison | 13,4 Mio. | 6,4 Mio. |

**Erledigt 05.10.2026:** Ergebnistexte neutral für alle Standorte, Würzburg-Fassungen neu erzeugt (Kontrollwerte identisch mit 01.10.2026).
