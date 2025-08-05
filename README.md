# Consulting Appointment GUI

A simple and extensible GUI project for managing consultants and scheduling appointments, with user role separation (Admin / Regular User).

---------

## Features

- Role-based access control: Admins can manage consultants & appointments; users can only view.
- Add, edit, delete appointments and consultants (admins only).
- Search functionality:
  - Search appointments by consultant or date.
  - Search consultants by name.
- GUI built with **Tkinter** and data stored in **JSON files**.

---------

## Screenshots

![Admin Panel - Consultant List](images\admin_panel.png)  
*Screenshot: Admin panel showing consultants list with edit/delete buttons.*


![User Panel - Appointments View](images\user_panel.png)  
*Screenshot: User panel viewing appointments without edit/delete permissions.*

---------

## Running the Project

Make sure you have **Python 3.8+** installed.

### 1. Clone the project

```bash
git clone https://github.com/arezookhalife/consulting_app_gui.git
cd consulting_app_gui

```
### 2. Set up a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Linux/macOS
venv\Scripts\activate        # On Windows

```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the project
```bash
python main.py
```
### Login Credentials
* Admin
    Username: admin
    Password: admin123

* Users
    User data is stored in the **users.json** file, and new users can be added to this file.

### Project Structure

```pgsql
CONSULTING_APP_GUI/
├── data/
│   ├── appointments.json
│   ├── consultants.json
│   └── users.json
├── forms/
│   ├── add_appointment.py
│   ├── add_consultant.py
│   ├── edit_appointments.py
│   ├── edit_consultant.py
│   ├── view_appointments.py
│   └── view_consultants.py   
├── logic/
│   ├── appointments.py
│   ├── auth.py
│   ├── consultants.py
│   └── utils.py
├── log.txt
├── login_window.py
├── main.py
├── panels.py
├── README.md
└── requirements.txt

```
### Future Improvements
* Connect to a real database (SQLite or PostgreSQL)
* Add email/SMS reminders for appointments
* Add appointment cancellation/editing options

### Developer
- Arezoo Khalifeh | Python Developer 
- GitHub: arezookhalife