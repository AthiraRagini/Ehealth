# MediCare Hub 🏥  
(Django Hospital Management System)

MediCare Hub is a **role-based healthcare management web application** built using **Django**.  
It connects **Patients, Doctors, and Admins** on a single platform to manage appointments, health records, payments, prescriptions, and video consultations.

---

## 🚀 Key Features

### 👤 Authentication & Roles
- Separate login & registration for:
  - Patients
  - Doctors
  - Admin (Staff users)
- Custom role-based access control using decorators

---

### 🧑‍⚕️ Doctor Module
- Doctor registration & login
- View assigned patients
- Accept / reject appointments
- View & update patient health data
- Add & edit prescriptions
- Start **Zoom video consultations**
- Edit doctor profile

---

### 🧑‍🦱 Patient Module
- Patient registration & login
- Book appointments by:
  - Doctor specialization
  - Doctor name search
- Upload personal health data
- View health alerts
- Pay consultation fees (Card + PIN simulation)
- Join **video consultations**
- View prescriptions & appointment history

---

### 📅 Appointment Management
- Appointment request & confirmation
- Doctor approval workflow
- Status tracking (Pending / Confirmed / Rejected)
- Payment-linked appointment confirmation

---

### 💳 Payment System
- Appointment-based payments
- Secure multi-step flow:
  - Card details
  - PIN verification
- Payment status tracking
- Transaction ID generation
- Revenue calculation for admin

---

### 📊 Health Records & Alerts
- Patient health data tracking
- Doctor-entered medical updates
- Automatic health alerts
- Admin & doctor access to patient reports

---

### 🧑‍💼 Admin Dashboard
- Admin login (staff only)
- View platform statistics:
  - Users
  - Patients
  - Doctors
  - Appointments
  - Payments
  - Revenue
- Manage users (patients & doctors)
- Edit or delete doctors & patients
- View all appointments & payments
- View patient health data

---

### 🎥 Video Consultation
- Zoom API integration
- Secure meeting creation
- Doctor starts meeting
- Patient joins after:
  - Appointment confirmation
  - Successful payment

---

## 🧰 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Django Templates
- **Database:** SQLite
- **Authentication:** Django Auth
- **Payments:** Simulated payment gateway
- **Video Calls:** Zoom API
- **ORM:** Django ORM
- **Version Control:** Git & GitHub

---



