# Usiamo un'immagine ufficiale di Python leggera
FROM python:3.10-slim

# Impostiamo la cartella di lavoro dentro il container
WORKDIR /app

# Copiamo e installiamo le dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiamo tutto il resto del codice del progetto dentro il container
COPY . .

# Apriamo la porta 8000 per le API
EXPOSE 8000

# Comando per avviare il server Uvicorn quando il container si accende
CMD ["uvicorn", "main_api:app", "--host", "0.0.0.0", "--port", "8000"]