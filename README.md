# 🔖 Bookmarks API with Authentication

<div align=center>

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![REST API](https://img.shields.io/badge/REST-API-0277BD?style=for-the-badge)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Passlib](https://img.shields.io/badge/Passlib-Password%20Hashing-795548?style=for-the-badge)

</div>


A powerful RESTful API for managing bookmarks with built-in authentication, built with FastAPI and SQLite.

## ✨ Features

- 🔐 **JWT Authentication** - Secure user authentication and authorization
- 📚 **Bookmark Management** - Create, read, update, and delete bookmarks
- 👤 **User Management** - User registration and profile management
- 🗄️ **SQLite Database** - Lightweight and efficient data storage
- 📝 **Automatic Documentation** - Interactive API docs with Swagger UI
- ⚡ **Fast Performance** - Built on FastAPI for high performance
- 🔒 **Password Hashing** - Secure password storage with bcrypt
- 🎯 **RESTful Design** - Clean and intuitive API endpoints

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/jusxtdev/Bookmarks-API-with-Auth.git
cd Bookmarks-API-with-Auth
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## 📖 API Documentation

Once the server is running, you can access:

- **Swagger UI Documentation**: `http://localhost:8000/docs`
- **ReDoc Documentation**: `http://localhost:8000/redoc`

## 🔑 API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get JWT token
- `POST /api/auth/refresh` - Refresh access token

### Bookmarks
- `GET /api/bookmarks` - Get all bookmarks (authenticated)
- `POST /api/bookmarks` - Create a new bookmark (authenticated)
- `GET /api/bookmarks/{id}` - Get a specific bookmark (authenticated)
- `PUT /api/bookmarks/{id}` - Update a bookmark (authenticated)
- `DELETE /api/bookmarks/{id}` - Delete a bookmark (authenticated)

### Users
- `GET /api/users/me` - Get current user profile (authenticated)
- `PUT /api/users/me` - Update user profile (authenticated)

## 🛠️ Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern web framework for building APIs
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - SQL toolkit and ORM
- **[SQLite](https://www.sqlite.org/)** - Embedded database
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Data validation using Python type hints
- **[python-jose](https://python-jose.readthedocs.io/)** - JWT tokens
- **[passlib](https://passlib.readthedocs.io/)** - Password hashing
- **[uvicorn](https://www.uvicorn.org/)** - ASGI server

## 📁 Project Structure

```
Bookmarks-API-with-Auth/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── models.py            # Database models
│   ├── schemas.py           # Pydantic schemas
│   ├── database.py          # Database configuration
│   ├── auth.py              # Authentication logic
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # Auth endpoints
│       ├── bookmarks.py     # Bookmark endpoints
│       └── users.py         # User endpoints
├── database.db              # SQLite database file
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

## 💡 Usage Example

### Register a new user
```bash
curl -X POST "http://localhost:8000/api/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "secure_password"
  }'
```

### Login
```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "secure_password"
  }'
```

### Create a bookmark
```bash
curl -X POST "http://localhost:8000/api/bookmarks" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "FastAPI Documentation",
    "url": "https://fastapi.tiangolo.com",
    "description": "Official FastAPI documentation"
  }'
```

## 🔒 Security

- Passwords are hashed using bcrypt before storage
- JWT tokens for secure authentication
- Protected endpoints require valid authentication
- Input validation with Pydantic models

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**jusxtdev**
- GitHub: [@jusxtdev](https://github.com/jusxtdev)

## 📧 Support

If you have any questions or issues, please open an issue on GitHub.

---

⭐ If you find this project helpful, please give it a star!