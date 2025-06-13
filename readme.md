
# FastAPI Blog Application 🚀

A full-featured backend application built using **FastAPI**, designed for managing users and blogs with authentication, database integration, and modern testing setup.

## 📌 Features

- 🔐 JWT Authentication (Login/Register)
- 🧑 User Management
- 📝 Blog Creation & Listing
- 🗃️ SQLAlchemy + Alembic for ORM & Migrations
- 🧪 Pytest for Unit Testing
- ✅ Pydantic for Request & Response Validation (v2 Compatible)
- 🌐 Auto-generated API Docs with Swagger (OpenAPI)
- 🧩 Modular Code Structure

---

## 📁 Project Structure

```
FastApi_Learning/
│
├── alembic/                 # Alembic migration folder
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions/            # Alembic migration scripts
├── apis/                    # API route definitions
│   ├── base.py
│   ├── route_blog.py
│   ├── route_login.py
│   └── route_user.py
├── app/                     # (Optional) Additional app logic/routes/templates
│   ├── base.py
│   ├── route_blog.py
│   ├── route_login.py
│   ├── static/              # Static files (css, js, images)
│   └── templates/           # Jinja2 or other templates
├── core/                    # Settings and core logic
│   ├── config.py
│   ├── hashing.py
│   └── security.py
├── db/                      # Database setup, models, repository
│   ├── base.py
│   ├── base_class.py
│   ├── models/              # SQLAlchemy models
│   ├── repository/          # Data access layer
│   └── session.py
├── schemas/                 # (No files listed; for Pydantic models)
├── tests/                   # Test cases
│   ├── conftest.py
│   └── test_routs/          # Test modules
├── alembic.ini              # Alembic config
├── main.py                  # App entrypoint
├── readme.md                # Project documentation
├── requirements.txt         # Python dependencies
└── sqlapp.db                # SQLite database (for development)
```

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/fastapi-blog.git
cd fastapi-blog
```

### 2. Setup Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Database & Run Migrations
```bash
alembic upgrade head
```

### 5. Run the App
```bash
uvicorn main:app --reload
```

Now visit: `http://127.0.0.1:8000/docs` to explore the API!

---

## 🧪 Running Tests

```bash
pytest
```

---

## ✅ Environment Variables (via `.env`)
```ini
DATABASE_URL=sqlite:///./test_db.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🙌 Contributions

PRs and suggestions are welcome! Make sure to format with `black` and add relevant test cases.

---

## 📃 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Akshat Thakkar**

---

> Built with ❤️ using FastAPI & SQLAlchemy.
