# 🧠 Predictive Analytics Core (PAC)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#) [![Coverage](https://img.shields.io/badge/coverage-94%25-green.svg)](#) [![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.103.1-009688.svg)](https://fastapi.tiangolo.com/)

## 📖 Overview
The **Predictive Analytics Core** is a high-performance microservice designed to ingest streaming data, run optimized machine-learning inference models, and serve predictive insights instantly via a scalable REST API. 

Built ground-up with an async-first architecture utilizing FastAPI, PostgreSQL, and Redis, this service is engineered to handle massive throughput while maintaining sub-50ms p99 latency for critical predictions.

---

## 🏗️ Architecture Stack

- **API Layer**: [FastAPI](https://fastapi.tiangolo.com/) handling asynchronous HTTP concurrency.
- **Data Persistence**: [PostgreSQL 15](https://www.postgresql.org/) for robust historical trend analysis and relational storage.
- **Caching & Queueing**: [Redis](https://redis.io/) handling rapid inference mapping and API rate limiting.
- **Infrastructure**: Fully Dockerized for seamless orchestration and scaling.

---

## 🚀 Quick Start

### Prerequisites
Before you begin, ensure you have the following installed:
* [Docker Component (24.0+)](https://www.docker.com/)
* [Python 3.11+](https://www.python.org/)

### Installation & Deployment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sushant-mutnale/predictive-analytics-core.git
   cd predictive-analytics-core
   ```

2. **Set up the environment:**
   ```bash
   # Copy the default configuration
   cp .env.example .env
   ```

3. **Spin up the infrastructure:**
   ```bash
   # Build and start the API, Postgres, and Redis containers in detached mode
   docker-compose up --build -d
   ```

4. **Verify Deployment:**
   The interactive Swagger UI documentation will now be available locally at:
   👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## 📡 Core API Reference

The service follows strict RESTful principles via `/api/v1/`.

| Endpoint | Method | Required Auth | Description |
|----------|--------|---------------|-------------|
| `/health` | `GET` | No | System ping for load balancers (Checks DB/Redis) |
| `/predict/batch` | `POST` | Yes | Submit JSON payload for synchronous model inference. |
| `/metrics/trend` | `GET` | Yes | Returns 30-day historical accuracy metrics. |
| `/users/auth` | `POST` | No | Exchange credentials for expiring Bearer JWT. |

*(For comprehensive endpoint coverage, view `/docs/api_reference.md`)*

---

## 🧪 Development & Testing

To run the local unit tests and integration suites using `pytest`:

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# Install dev dependencies
pip install -r requirements.txt

# Execute test suite
pytest tests/ -v --disable-warnings
```

## 📜 License
Proprietary source. All rights reserved.
