# MTailor MLOps Assessment

## Project Overview

This project demonstrates deploying a simple **classification neural network** on **Cerebrium’s serverless GPU platform**.

The API is deployed and tested successfully using Cerebrium’s endpoint.

---

## Project Structure

| File | Purpose |
|------|---------|
| `predict.py` | Model API code for deployment on Cerebrium |
| `test_api.py` | Test script for invoking the deployed API |
| `requirements.txt` | Project dependencies |
| `.gitignore` | Ignore unnecessary files (including `.env`) |
| `.env` | Contains Bearer token for API (not committed to GitHub) |

---

## How to Setup & Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/mtailor_mlops_assessment.git
cd mtailor_mlops_assessment
```

### 2️⃣ Set Up Virtual Environment 
```bash
python3 -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate  # For Linux/Mac
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure .env

```bash
BEARER_TOKEN=your_cerebrium_bearer_token_here
```
### 5️⃣ Run API Test Script

```bash
python test_api.py
```
## Deployment on Cerebrium

Project deployed on Cerebrium# MTailor MLOps Assessment

## Project Overview

This project demonstrates deploying a simple **classification neural network** on **Cerebrium’s serverless GPU platform**.

The API is deployed and tested successfully using Cerebrium’s endpoint.

---

## Project Structure

| File | Purpose |
|------|---------|
| `predict.py` | Model API code for deployment on Cerebrium |
| `test_api.py` | Test script for invoking the deployed API |
| `requirements.txt` | Project dependencies |
| `.gitignore` | Ignore unnecessary files (including `.env`) |
| `.env` | Contains Bearer token for API (not committed to GitHub) |

---

## How to Setup & Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/mtailor_mlops_assessment.git
cd mtailor_mlops_assessment
```

### 2️⃣ Set Up Virtual Environment 
```bash
python3 -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate  # For Linux/Mac
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure .env

```bash
BEARER_TOKEN=your_cerebrium_bearer_token_here
```
### 5️⃣ Run API Test Script

```bash
python test_api.py
```
## Deployment on Cerebrium

Project deployed on Cerebrium [https://www.cerebrium.ai/]. 

## Notes
1. Bearer token is securely stored in .env and used via python-dotenv

2. API tested with both CLI and test_api.py


## Notes
1. Bearer token is securely stored in .env and used via python-dotenv

2. API tested with both CLI and test_api.py
