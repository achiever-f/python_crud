# Employee Management System

A comprehensive CRUD (Create, Read, Update, Delete) web application built with Django and Bootstrap for managing employee records efficiently.

## 📋 Table of Contents

- [Employee Management System](#employee-management-system)
  - [📋 Table of Contents](#-table-of-contents)
  - [✨ Features](#-features)
  - [🛠 Technologies Used](#-technologies-used)
    - [Backend](#backend)
    - [Frontend](#frontend)
    - [Development Tools](#development-tools)
  - [📁 Project Structure](#-project-structure)
  - [📦 Installation](#-installation)
  - [🚀 Usage](#-usage)
  - [📄 File Documentation](#-file-documentation)
  - [📡 API Endpoints](#-api-endpoints)
  - [🗄️ Database Models](#️-database-models)

## ✨ Features

- **Employee Management**: Create, read, update, and delete employee records
- **Responsive Design**: Mobile-friendly Bootstrap 5 interface with modern styling
- **Form Validation**: Client-side and server-side validation for data integrity
- **Security**: CSRF protection on all forms
- **Search & Navigation**: Easy navigation with breadcrumbs and menu items
- **Professional UI/UX**: Gradient backgrounds, smooth transitions, and intuitive layout
- **Real-time Feedback**: Visual feedback on form submissions and operations

## 🛠 Technologies Used

### Backend

- **Django 4.2+**: Python web framework for backend logic
- **Python 3.12**: Programming language
- **SQLite**: Default database (configurable)

### Frontend

- **Bootstrap 5.3**: CSS framework for responsive design
- **Bootstrap Icons 1.11**: Icon library
- **HTML5**: Markup structure
- **CSS3**: Custom styling with gradients and animations

### Development Tools

- **Django ORM**: Object-relational mapping for database queries
- **Django Templates**: Template engine for dynamic HTML rendering
- **Django Static Files**: Static file management

## 📁 Project Structure

```
employee_management_system/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── employee_crud/                  # Main Django app
│   ├── migrations/                 # Database migrations
│   ├── __init__.py
│   ├── admin.py                    # Admin panel configuration
│   ├── apps.py
│   ├── models.py                   # Database models
│   ├── tests.py                    # Automated tests
│   └── views.py                    # Request handlers
│
├── employee_management/            # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                 # Main configuration
│   ├── urls.py                     # URL routing
│   └── wsgi.py
│
└── templates/                     # HTML templates
    ├── base.html                  # Base template
    ├── employee_list.html         # Employee listing
    ├── employee_form.html         # Employee form
    └── ...                        # Other templates
```

## 📦 Installation

1. **Clone the repository**:
   ``` bash
   git clone https://github.com/yourusername/employee_management_system.git
   cd employee_management_system
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (admin account):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/`

## 🚀 Usage

- **Accessing the app**: Navigate to the app URL in your browser.
- **Admin panel**: Access the admin panel at `/admin` to manage employees.
- **CRUD operations**: Use the provided UI to create, read, update, and delete employee records.

## 📄 File Documentation

- **`manage.py`**: Django project management script.
- **`db.sqlite3`**: SQLite database file.
- **`requirements.txt`**: Python package dependencies.
- **`employee_crud/`**: Main Django app directory.
- **`employee_management/`**: Project settings and configuration.
- **`templates/`**: Directory for HTML templates.

## 📡 API Endpoints

- **`GET /api/employees/`**: Retrieve a list of employees.
- **`POST /api/employees/`**: Create a new employee record.
- **`GET /api/employees/{id}/`**: Retrieve a specific employee by ID.
- **`PUT /api/employees/{id}/`**: Update a specific employee by ID.
- **`DELETE /api/employees/{id}/`**: Delete a specific employee by ID.

## 🗄️ Database Models

- **Employee**: Represents an employee record.
  - `id`: Auto-incrementing primary key.
  - `first_name`: Employee's first name.
  - `last_name`: Employee's last name.
  - `email`: Employee's email address.
  - `phone`: Employee's phone number.
  - `hire_date`: Date when the employee was hired.
  - `job_title`: Title of the employee's job.
  - `salary`: Employee's salary.
