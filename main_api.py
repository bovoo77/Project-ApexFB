from fastapi import FastAPI, HTTPException
import fastf1
import pandas as pd
from sqlalchemy import create_engine, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurazione del Database SQLite locale
DATABASE_URL = "sqlite:///./telemetry.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definizione della tabella SQL per la telemetria


class TelemetryModel(Base):
    __tablename__ = "telemetry_data"
    id = Column(Integer, primary_key=True, index=True)
    driver = Column(String, index=True)
    distance = Column(Float)
    speed = Column(Float)
    throttle = Column(Float)
    brake = Column(Float)
    gear = Column(Integer)


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Project Apex - F1 Telemetry API & DB", version="2.0")
fastf1.Cache.enable_cache('cache_folder')


@app.get("/")
def read_root():
    return {"status": "online", "message": "Database & API di Project Apex attivi per Unibo Motorsport!"}


@app.get("/api/v1/load-to-db")
def load_data_to_database():
    """Scarica i dati di Leclerc dal Bahrain e li salva nel database SQL"""
    session = fastf1.get_session(2024, 'Bahrain', 'R')
    session.load(telemetry=True, weather=False, messages=False)

    # Usiamo pick_drivers come suggerito dal warning
    leclerc_laps = session.laps.pick_drivers('LEC')
    fastest_lap = leclerc_laps.pick_fastest()
    telemetry = fastest_lap.get_telemetry()

    db = SessionLocal()
    db.query(TelemetryModel).delete()

    for _, row in telemetry.head(100).iterrows():
        # Gestiamo il campo marcia in modo sicuro (cercando 'Gear' o 'nGear')
        gear_val = row.get('Gear', row.get('nGear', 0))

        db_item = TelemetryModel(
            driver="LEC",
            distance=row.get('Distance', 0.0),
            speed=row.get('Speed', 0.0),
            throttle=row.get('Throttle', 0.0),
            brake=row.get('Brake', 0.0),
            gear=int(gear_val) if pd.notna(gear_val) else 0
        )
        db.add(db_item)

    db.commit()
    db.close()
    return {"message": "Successo! Dati di telemetria salvati permanentemente nel database SQL."}


@app.get("/api/v1/telemetry/db")
def get_telemetry_from_db():
    """Legge i dati direttamente dal database SQL (senza ricaricare FastF1)"""
    db = SessionLocal()
    data = db.query(TelemetryModel).all()
    db.close()

    if not data:
        raise HTTPException(
            status_code=404, detail="Database vuoto! Esegui prima /api/v1/load-to-db")

    return {"source": "SQLite Database", "rows_returned": len(data), "data": data}
