# Smart Classroom Timetable Management System

A web-based application built with Flask to manage, view, and organize classroom schedules. The system provides separate interfaces for administrators and students, with features for automatic substitute assignment and timetable exporting.

# 📜 Project Overview
The Smart Classroom system is designed to streamline the process of academic scheduling. Administrators have full control over the weekly timetable, with the ability to add, delete, and modify lectures. A key feature is the **Add Substitute** function, which intelligently finds an available teacher of the same subject to cover a class.

Students can log in to view their personal, section-specific timetable, which is always up-to-date. They also have the option to download their schedule in user-friendly formats like PDF and Excel for offline access.

# ✨ Key Features
- **Role-Based Access Control:** Separate, secure login and dashboard views for Administrators and Students.
- **Admin Dashboard:** A comprehensive interface to manage the entire weekly schedule.
- Add and delete lectures.
- View all sections and teachers at a glance.
- **Intelligent Substitute Assignment:** Automatically finds and assigns an available teacher of the same subject when a substitute is needed.
- **Student Dashboard:** A clean, easy-to-read view of the student's personal weekly timetable, sorted by day.
- **Timetable Export:** Students can download their personal timetable in two convenient formats:
- **PDF:** A grid-based, print-friendly document.
- **Excel:** A fully formatted .xlsx spreadsheet.
- **Modular & Scalable:** Built using Flask Blueprints and a service-oriented structure for easy maintenance and future expansion.

# 🛠️ Tech Stack
- **Backend:** Flask, Flask-SQLAlchemy, Flask-Login
- **Database:** SQLite
- **PDF Generation:** ReportLab
- **Excel Generation:** Openpyxl
- **Frontend:** HTML, CSS (with Jinja2 for templating)

# 🚀 Setup and Installation
To get the project running locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/vush-man/SmartEdu-Planner.git
cd SmartEdu-Planner
```

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

### For Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### For macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all the required packages from your requirements.txt file.
```bash
pip install -r requirements.txt
```

### 4. Initialize the Database
Run the seeding script to create the database file (smartclassroom.db) and populate it with initial sample data, including user accounts, teachers, and a sample schedule.
```bash
python seed_db.py
```

### 5. Run the Application
Start the Flask development server.
```bash
python run.py
```
# Default login credentials
### For Student
- **ID 1:** studentA
**Password:** student

**ID 2:** studentB
**Password:** student

### For Admin
**ID:** admin
**Password:** admin






