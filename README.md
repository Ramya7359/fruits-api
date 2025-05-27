# Fruits API

A simple, FastAPI-based microservice to manage a list of fruits — complete with persistent storage, automated testing, and CI/CD pipeline.

---

##  Features

- **GET /fruits** – List all fruits
- **GET /fruits/{id}** – Get a fruit by its ID
- **POST /fruits** – Add a new fruit (expects JSON)

### Example Request Payload

```json
{
  "fruit": "apple",
  "color": "red"
}
````

---

## Example JSON Response

```json
[
  {
    "id": 1,
    "fruit": "apple",
    "color": "red"
  }
]
```

---

## Tech Stack

* Python + FastAPI
* SQLite + SQLAlchemy
* Pytest for testing
* Docker for containerization
* GitHub Actions for CI/CD

---

## Installation & Usage

### Local Setup

```bash
# Clone the repo
git clone https://github.com/Ramya7359/fruits-api.git
cd fruits-api

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run the API Server

```bash
uvicorn app.main:app --reload
```

---

##  Run Tests

```bash
PYTHONPATH=. pytest
```

---

## Docker

###  Build Docker Image

```bash
docker build -t fruits-api .
```

### ▶Run Container

```bash
docker run -p 8000:8000 fruits-api
```
Verify : http://localhost:8000/docs

<img width="950" alt="image" src="https://github.com/user-attachments/assets/30a715d1-011a-4cd9-b337-202b5034adf3" />

---

## CI/CD Pipeline

This project uses **GitHub Actions** to:

* Run tests
* Build Docker image
* Push to Docker Hub (or GitHub Container Registry)
* Workflow File: .github/workflows/ci.yml

```
 name: CI

on:
  push:
    branches: [ master ]

jobs:
  build-test-publish:
    runs-on: self-hosted

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
        check-latest: true
        update-environment: true

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        export PYTHONPATH="${{ github.workspace }}"
        pytest

    - name: Build Docker image with SHA and latest tags
      run: |
        IMAGE_TAG=${{ github.sha }}
        docker build -t ramyamo/fruits-api:${IMAGE_TAG} -t ramyamo/fruits-api:latest .

    - name: Log in to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}

    - name: Push Docker images (SHA and latest)
      run: |
        IMAGE_TAG=${{ github.sha }}
        docker push ramyamo/fruits-api:${IMAGE_TAG}
        docker push ramyamo/fruits-api:latest
```
