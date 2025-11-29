# 🏥 Hospital Management System

A comprehensive web-based Hospital Management System built with Flask, designed for efficient management of patients, doctors, appointments, and medical records.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Milestones](#milestones)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### 🔐 Authentication & Authorization
- Secure user login system with password hashing
- Role-based access control (Admin, Doctor, Patient)
- Session management with 24-hour persistence
- Patient self-registration

### 👨‍💼 Admin Panel
- Dashboard with real-time statistics
- Complete doctor management (Add/Edit/Delete)
- Patient management (View/Remove)
- View all appointments (upcoming and past)
- Search doctors by name or specialization
- Search patients by name, ID, or contact
- Professional table layouts with actions

### 🩺 Doctor Portal
- View scheduled appointments
- Access patient medical records
- Track completed appointments
- Dashboard with statistics

### 👤 Patient Portal
- Self-registration system
- View upcoming appointments
- Access medical history
- User-friendly dashboard

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.13** | Backend programming language |
| **Flask** | Web framework |
| **SQLAlchemy** | ORM for database operations |
| **SQLite** | Database |
| **HTML5/CSS3** | Frontend structure and styling |
| **Bootstrap 5** | Responsive UI framework |
| **Jinja2** | Template engine |
| **Werkzeug** | Password hashing & security |

---

## 📁 Project Structure

hospital_management/
│
├── app.py # Main application file (routes, models)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Git ignore rules
│
├── instance/
│ └── site.db # SQLite database
│
└── templates/
├── base.html # Base template with navbar
├── home.html # Landing page
├── login.html # Login page
├── register.html # Patient registration
│
├── admin/
│ ├── dashboard.html # Admin dashboard
│ ├── add_doctor.html # Add doctor form
│ ├── view_doctors.html # Doctors list
│ ├── edit_doctor.html # Edit doctor
│ ├── view_patients.html # Patients list
│ ├── view_appointments.html # All appointments
│ ├── search_doctors.html # Search doctors
│ └── search_patients.html # Search patients
│
├── doctor/
│ └── dashboard.html # Doctor dashboard
│
└── patient/
└── dashboard.html # Patient dashboard
---
## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Steps

1. **Clone the repository:**  git clone https://github.com/24f2006737/Hospital-Management-App.git  cd Hospital-Management-App

2. **Create virtual environment:**  python -m venv venv

3. **Activate virtual environment:**  **Windows:**   venv\Scripts\activate

4. **Install dependencies:** pip install flask flask-sqlalchemy werkzeug

5. **Run the application:**        python app.py
   
6. **Access the application:**     http://127.0.0.1:5000



---

## 💻 Usage

### Default Credentials

**Admin Login:**
- Username: `admin`
- Password: `admin123`
- Access: Full system control

**Patient:**
- Register at: `/register`
- Login at: `/login`

**Doctor:**
- Created by admin only
- Login with credentials provided by admin

### Important Routes

| Route | Access | Description |
|-------|--------|-------------|
| `/` | Public | Home page |
| `/login` | Public | Login page |
| `/register` | Public | Patient registration |
| `/logout` | Authenticated | Logout |
| `/admin/dashboard` | Admin | Admin dashboard |
| `/admin/doctors` | Admin | View all doctors |
| `/admin/patients` | Admin | View all patients |
| `/admin/appointments` | Admin | View all appointments |
| `/admin/search-doctors` | Admin | Search doctors |
| `/admin/search-patients` | Admin | Search patients |
| `/doctor/dashboard` | Doctor | Doctor dashboard |
| `/patient/dashboard` | Patient | Patient dashboard |

---

## 🗄️ Database Schema

### Tables

**1. Users**
- `id` (Primary Key)
- `username` (Unique)
- `email` (Unique)
- `password` (Hashed)
- `role` (admin/doctor/patient)
- `created_at` (Timestamp)

**2. Departments**
- `id` (Primary Key)
- `name` (Unique)
- `description`
- `created_at` (Timestamp)

**3. Patients**
- `id` (Primary Key)
- `name`
- `age`
- `gender`
- `contact`
- `address`

**4. Doctors**
- `id` (Primary Key)
- `name`
- `specialization`
- `contact`
- `department_id` (Foreign Key → departments)

**5. Appointments**
- `id` (Primary Key)
- `patient_id` (Foreign Key → patients)
- `doctor_id` (Foreign Key → doctors)
- `date`
- `time`
- `status` (Booked/Completed/Cancelled)
- `notes`
- `created_at` (Timestamp)

**6. Treatments**
- `id` (Primary Key)
- `appointment_id` (Foreign Key → appointments)
- `diagnosis`
- `prescription`
- `notes`
- `treatment_date` (Timestamp)

### Relationships

Department (1) ──→ (Many) Doctor
Patient (1) ──→ (Many) Appointment
Doctor (1) ──→ (Many) Appointment
Appointment (1) ──→ (Many) Treatment



---

## 🎯 Milestones

### ✅ Milestone 1: Database Models & Schema Setup
**Status:** Complete  
**Commit:** `Milestone-HMS DB-Relationship`  
**Date:** November 25, 2025

- [x] User model with authentication
- [x] Patient, Doctor, Department models
- [x] Appointment and Treatment models
- [x] Database relationships established
- [x] Programmatic database creation

### ✅ Milestone 2: Authentication & Role-Based Access Control
**Status:** Complete  
**Commit:** `Milestone-HMS Auth-RBAC`  
**Date:** November 28, 2025

- [x] Secure login system
- [x] Patient self-registration
- [x] Admin, Doctor, Patient dashboards
- [x] Role-based route protection
- [x] Session management
- [x] Password hashing with Werkzeug
- [x] Flash messages for user feedback
- [x] Professional UI design

### ✅ Milestone 3: Admin Dashboard & Management
**Status:** Complete  
**Commit:** `Milestone-HMS Admin-Dashboard-Management`  
**Date:** November 29, 2025

- [x] Admin dashboard with real-time statistics
- [x] View all doctors with edit/delete functionality
- [x] Update doctor profiles
- [x] View all patients with delete option
- [x] View all appointments (upcoming and past)
- [x] Search doctors by name or specialization
- [x] Search patients by name, ID, or contact
- [x] Professional table layouts
- [x] Confirmation dialogs for deletions
- [x] Remove doctors/patients from system


---

## 📸 Screenshots

### Admin Dashboard
![Admin Dashboard](screenshots/admin-dashboard.png)
*Admin portal showing statistics and quick actions*

### Doctor Management
![View Doctors](screenshots/view-doctors.png)
*Complete doctor list with edit and delete options*

### Search Functionality
![Search](screenshots/search-doctors.png)
*Search doctors by name or specialization*

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📧 Contact

**Developer:** IITM BS Student (Data Science & Applications)  
**GitHub:** https://github.com/dashboard  
**Project Link:** [Hospital Management App] https://github.com/24f2006737/Hospital-Management-App

---

## 📄 License

This project is part of IITM BS Degree coursework.

---

## 🙏 Acknowledgments

- IITM BS Degree Program
- Flask Documentation
- Bootstrap Documentation
- SQLAlchemy Documentation
- Stack Overflow Community

---

## 📊 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/24f2006737/Hospital-Management-App)
![GitHub last commit](https://img.shields.io/github/last-commit/24f2006737/Hospital-Management-App)
![GitHub contributors](https://img.shields.io/github/contributors/24f2006737/Hospital-Management-App)

**Current Progress:** 60% (3/5 Milestones Complete)

---

**Made with ❤️ for IITM BS Degree Project**
