# 🚀 FastAPI Scaffold with Request Limiter and Testing Utilities

This repository provides a scaffold to set up **FastAPI** with request limiting and performance testing using **Locust**.

---

![FastAPI Logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)  
<sup><sub>*FastAPI framework for Python.*</sub></sup>

## 📋 Prerequisites
- 🐍 **Python** 3.8 - 3.12
- 🐳 **Docker** (optional for devcontainer setup)

## ⚙️ Setup

### Option 1: Devcontainer (Visual Studio Code)
1. Open the project in **VS Code**.
2. Use the configuration in `.devcontainer/devcontainer.json`.
3. Required dependencies in `requirements.txt` are auto-installed.

https://code.visualstudio.com/docs/devcontainers/tutorial

### Option 2: Virtual Environment
1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
2. Activate it:
    - **Windows:**
        ```sh
        .\venv\Scripts\activate
        ```
    - **macOS/Linux:**
        ```sh
        source venv/bin/activate
        ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## ▶️ Running the Application
Use the Makefile to start services:
- **FastAPI server:** `make start_fastapi`
- **Locust web interface:** `make start_locust`

---

## 📂 Key Files and Structure
- **FastAPI:** Configured in `main.py` with CORS, request limiting (`slowapi`), and example routes.
- **Locust:** Performance tests in `locustfile.py`.

<details>
  <summary>📁 Project Structure</summary>
  
