# Project Apex - F1 Telemetry Data Platform

A modular, containerized back-end application developed for motorsport telemetry analysis. Project Apex extracts official Formula 1 session data, processes it through a REST API, ensures persistence via a relational database, and guarantees cross-platform portability through containerization.

## Key Features

* Data Pipeline (ETL): Extracts and structures metrics (speed, throttle, brake, gear, distance) using the FastF1 library.
* REST API: Built with FastAPI providing asynchronous endpoints and Swagger UI documentation.
* Database Persistence: Permanent storage and querying of telemetry data via SQLite and SQLAlchemy ORM.
* Containerization: Fully packaged with Docker for consistent execution across environments.

## Tech Stack

* Language: Python 3.10+
* Framework: FastAPI, Uvicorn
* Data Engineering: FastF1, Pandas
* Database: SQLite, SQLAlchemy
* DevOps: Docker

## Installation and Running

### Local Setup
1. Clone the repository and navigate to the folder:
   git clone https://github.com/bovoo77/Project-ApexFB.git
   cd Project-ApexFB
3. Create and activate a virtual environment, then install dependencies:
   python -m venv venv
   source venv/Scripts/activate
   pip install -r requirements.txt
4. Run the server:
   uvicorn main_api:app --reload
5. Access documentation at http://127.0.0.1:8000/docs

### Docker Setup
1. Build the image:
   docker build -t project-apex-api .
2. Run the container:
   docker run -d -p 8000:8000 --name apex-container project-apex-api

## API Endpoints

* GET /api/v1/load-to-db: Triggers the telemetry pipeline, extracts driver session data, and saves it to the SQLite database.
* GET /api/v1/telemetry/db: Queries the relational database and returns stored telemetry records in JSON format.
