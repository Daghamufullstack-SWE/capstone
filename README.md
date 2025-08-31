# Scool Data Integrated System - SCODIS

RESTful API system for secondary school managent built with Django and Django REST Framework. The platform facilitates parent/guardian engagement in students academics through guardian portal where thay can view student's attendance, performance and payments status.

## 🚀 Features

- **Guardian Portal**: Parents/Guadian have access to stuents acaemic records and pay fees
- **User registration**: Complete CRUD operations for admin to register schools, students and staff members
- **User Authentication**: JWT-based authentication with registration, login, and profile management
- **Admin Dashboard**: Comprehensive administrative tools for content and user management
- **RESTful Architecture**: Clean, standardized API endpoints following REST principles

## 📋 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/users/` | GET, POST | List and create users |
| `/api/user/<pk>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete specific user |
| `/portal/guardian/` | GET, POST | SCODIS dashboard to authenticated guardian |
| `/api/finance/` | GET, PUT Manage specific payment |
| `/api/departments/` | GET, POST | List and create departments |
| `/api/subject/` | GET, POST, DELETE | Manage specific subject |
|
## 🛠️ Technology Stack

- **Backend Framework**: Django 3.2
- **API Framework**: Django REST Framework 3.12
- **Database**: SQLite 
- **Authentication**: Token Authentication, Simple_JWT_Token
- **Python Version**: 3.8

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ydaghamuFullstack-swe/capstone.git
   cd capstone/scodis
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
NEWS_API_KEY=your-newsapi-key
```

### External API Integration

.
.
.

## 🎯 Usage

### Authentication

```bash
# Register new user
curl -X POST http://localhost:8000/api/user/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "123", "email": "user@scodis.com"}'

# Login
curl -X POST http://localhost:8000/api/user/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "123"}'

# Use token in subsequent requests
curl -H "Authorization: Token <your-token>" http://localhost:8000/portal/guardian
```

### Creating a account

```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Authorization: Token <your-token>" \
  -H "Content-Type: application/json" \
  -d '{__fill in fields as prompted__}' 
```

## 🤝 Contributing

.
.
.
