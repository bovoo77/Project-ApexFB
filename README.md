# Project Apex - F1 Telemetry Data Platform

A modular, containerized back-end application developed for motorsport telemetry analysis. Project Apex extracts official Formula 1 session data, processes it through a REST API, ensures persistence via a relational database, and guarantees cross-platform portability through containerization.

## Key Features

* **Data Pipeline (ETL):** Extracts and structures metrics (speed, throttle, brake, gear, distance) using the FastF1 library.
* **REST API:** Built with FastAPI providing asynchronous endpoints and Swagger UI documentation.
* **Database Persistence:** Permanent storage and querying of telemetry data via SQLite and SQLAlchemy ORM.
* **Containerization:** Fully packaged with Docker for consistent execution across environments.

## Tech Stack

* **Language:** Python 3.10+
* **Framework:** FastAPI, Uvicorn
* **Data Engineering:** FastF1, Pandas
* **Database:** SQLite, SQLAlchemy
* **DevOps:** Docker

## Installation & Running

### Local Setup
1. Clone the repository and navigate to the folder:
   ```bash
   git clone [https://github.com/bovoSfasciaCarrozze/Project-ApexFB.git](https://github.com/bovoSfasciaCarrozze/Project-ApexFB.git)
   cd Project-ApexFB
