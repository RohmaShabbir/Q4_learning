# FastAPI Project – `fastdca-p1`

This is a simple FastAPI project created using `uv` for managing environment and dependencies. It includes a basic REST API with two endpoints to demonstrate FastAPI features.

## 🚀 Project Structure

```
fastdca-p1/
├── .venv/                  # Virtual environment
├── .python-version         # Python version file
├── main.py                 # FastAPI application
├── pycache/                # Python cache (auto-generated)
├── project/                # (Optional project files directory)
├── README.md               # Project README
└── uv.lock                 # uv dependencies lock file
```

---

## 🔧 Setup Instructions

### Step 1: Initialize the Project

```bash
uv init fastdca-p1
cd fastdca-p1
```

### Step 2: Create Virtual Environment

```bash
uv venv
# Activate the virtual environment (Windows)
.venv\Scripts\activate
```

### Step 3: Add Dependencies

```bash
uv add "fastapi[standard]"
```

This installs:

* `fastapi`
* `uvicorn` (ASGI server)
* other useful dependencies for web development.

---

## ✨ Create the API

Edit the `main.py` file with the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

---

## ▶️ Run the Server

To run the development server, use:

```bash
fastapi dev main.py
```

Visit:

* `http://localhost:8000` to access the root endpoint.
* `http://localhost:8000/items/42?q=test` to test the item endpoint.

---

## 🛠 Technologies Used

* Python 3.11+
* FastAPI
* uv (for dependency management)
* Uvicorn (ASGI server)

---

## 📄 License

This project is for educational purposes and personal learning.

---

Let me know if you’d like to add a database, authentication, or deploy it online!
