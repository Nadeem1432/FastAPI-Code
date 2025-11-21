# 📒 Address Book API (FastAPI + SQLModel)

A minimal **Address Book API** built with **FastAPI** and **SQLModel**.  
This API allows users to:
- Create, update, and delete addresses.
- Store addresses in an **SQLite** database.
- Validate input automatically using **SQLModel**.
- Retrieve addresses within a given distance from specified coordinates.

---

## 🚀 Features
- **CRUD Operations** for addresses.
- **SQLite database** for persistence.
- **Swagger UI** for API documentation.

---

## 🛠 Tech Stack
- https://fastapi.tiangolo.com/
- [SQLModel](https://sqlmodel.tiangolo.com/)
- https://www.sqlite.org/

---
## ⚙️ Setup

Follow these steps to set up the project:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Nadeem1432/FastAPI-Code.git
    cd FastAPI-Code
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    uvicorn app.main:app --reload
    ```

5. **Access the API documentation**:
    Open your browser and navigate to `http://127.0.0.1:8000/docs` to explore the Swagger UI.

---
