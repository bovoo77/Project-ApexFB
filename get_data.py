import fastf1
import pandas as pd

# 1. Abilitiamo la cache locale (così la prima volta scarica da internet, le prossime volte legge dal PC)
fastf1.Cache.enable_cache('cache_folder')

# 2. Carico la sessione: prendiamo ad esempio la Gara di Monza 2024
# Anno, Gran Premio, Sessione ('R' = Race, 'Q' = Qualifying)
session = fastf1.get_session(2024, 'Monza', 'R')
session.load()

# 3. Prendo i dati di un pilota specifico
leclerc_laps = session.laps.pick_driver('LEC')

# Prendo il giro più veloce di Leclerc
fastest_lap = leclerc_laps.pick_fastest()

# Estraggo la telemetria dettagliata di quel giro (velocità, marcia, RPM, freno, acceleratore)
telemetry = fastest_lap.get_telemetry()

print("\n--- scaricati dati con successo! ---")
print(telemetry.head())
