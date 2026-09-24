# 🏥 Doctor and Patient Management API

A simple **REST API** built using **Python and FastAPI** to manage doctors and patients.

This project demonstrates:

* REST API development
* FastAPI
* Pydantic data validation
* Email validation
* Error handling using `HTTPException`
* In-memory data storage
* Swagger API documentation

---

## 🛠️ Technologies Used

| Technology            | Purpose                              |
| --------------------- | ------------------------------------ |
| **Python 3.9+**       | Programming language                 |
| **FastAPI**           | Web framework for building REST APIs |
| **Pydantic**          | Data validation                      |
| **Uvicorn**           | ASGI server                          |
| **Email Validator**   | Email format validation              |
| **In-memory storage** | Temporary data storage               |

---

# 📁 Project Structure

```text
fastapi_doctor_patient/
│
├── main.py
├── requirements.txt
└── README.md
```

### File Description

* **`main.py`** → Contains the FastAPI application and API endpoints.
* **`requirements.txt`** → Contains the required Python packages.
* **`README.md`** → Contains project documentation and setup instructions.

---

# 🚀 Installation and Setup

## Step 1: Check Python Version

Open **Command Prompt** and run:

```bash
python --version
```

Python version should be **3.9 or above**.

Example:

```text
Python 3.11.5
```

---

## Step 2: Open the Project Folder

Open Command Prompt and navigate to the project folder.

Example:

```bash
cd Desktop\fastapi_doctor_patient
```

You can verify that `main.py` exists by running:

```bash
dir
```

You should see:

```text
main.py
requirements.txt
README.md
```

---

## Step 3: Install Required Packages

Install the required packages using:

```bash
pip install fastapi uvicorn email-validator
```

### Or install using `requirements.txt`

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the FastAPI server using:

```bash
python -m uvicorn main:app --reload
```

You should see something similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

> **Important:** Keep the Command Prompt open while using the API.

---

# 🌐 Open the API in Browser

Open your web browser and visit:

```text
http://127.0.0.1:8000
```

For testing the API, use the **FastAPI Swagger UI**:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides an interactive interface where you can test all API endpoints directly from your browser.

---

# 📚 API Endpoints

## 👨‍⚕️ Doctor APIs

### 1. Create Doctor

**Method:**

```text
POST
```

**Endpoint:**

```text
/doctors
```

### Request Body

```json
{
  "name": "Dr. Jaswanth",
  "specialization": "Cardiology",
  "email": "jashu@gmail.com",
  "is_active": true
}
```

### Expected Response

```json
{
  "message": "Doctor created successfully",
  "doctor": {
    "id": 1,
    "name": "Dr. Jaswanth",
    "specialization": "Cardiology",
    "email": "jashu@gmail.com",
    "is_active": true
  }
}
```

---

### 2. Get All Doctors

**Method:**

```text
GET
```

**Endpoint:**

```text
/doctors
```

### Example Response

```json
{
  "message": "Doctors retrieved successfully",
  "doctors": [
    {
      "id": 1,
      "name": "Dr. Jaswanth",
      "specialization": "Cardiology",
      "email": "jashu@gmail.com",
      "is_active": true
    }
  ]
}
```

---

### 3. Get Doctor by ID

**Method:**

```text
GET
```

**Endpoint:**

```text
/doctors/{doctor_id}
```

### Example

```text
/doctors/1
```

### Example Response

```json
{
  "id": 1,
  "name": "Dr. Jaswanth",
  "specialization": "Cardiology",
  "email": "jashu@gmail.com",
  "is_active": true
}
```

---

# 🧑‍⚕️ Patient APIs

### 1. Create Patient

**Method:**

```text
POST
```

**Endpoint:**

```text
/patients
```

### Request Body

```json
{
  "name": "Priya",
  "age": 20,
  "phone": "9876543210"
}
```

### Expected Response

```json
{
  "message": "Patient created successfully",
  "patient": {
    "id": 1,
    "name": "Priya",
    "age": 20,
    "phone": "9876543210"
  }
}
```

---

### 2. Get All Patients

**Method:**

```text
GET
```

**Endpoint:**

```text
/patients
```

### Example Response

```json
{
  "message": "Patients retrieved successfully",
  "patients": [
    {
      "id": 1,
      "name": "Priya",
      "age": 20,
      "phone": "9876543210"
    }
  ]
}
```

---

# ✅ Validation

The application uses **Pydantic models** to validate incoming data.

---

## 📧 Email Validation

The doctor's email must be in a valid email format.

### Valid Email

```text
jashu@gmail.com
```

### Invalid Email

```text
jashu123
```

The Doctor model uses:

```python
email: EmailStr
```

If an invalid email is provided, FastAPI returns:

```text
422 Unprocessable Entity
```

---

## 🎂 Age Validation

The patient's age must be **greater than 0**.

### Valid

```text
20
```

```text
1
```

### Invalid

```text
0
```

```text
-5
```

The Patient model uses:

```python
age: int = Field(gt=0)
```

`gt=0` means the value must be **greater than 0**.

If an invalid age is provided, FastAPI returns:

```text
422 Unprocessable Entity
```

---

# ❌ Error Handling

The application uses FastAPI's `HTTPException` for handling errors.

## Doctor Not Found

If you request a doctor ID that does not exist:

```text
GET /doctors/999
```

The API returns:

```json
{
  "detail": "Doctor not found"
}
```

Status code:

```text
404 Not Found
```

The application also automatically handles validation errors using **FastAPI and Pydantic**.

---

# 🧪 Testing the API

All APIs can be tested using the FastAPI Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Test 1: Create Doctor

Use:

```text
POST /doctors
```

Request:

```json
{
  "name": "Dr. Jaswanth",
  "specialization": "Cardiology",
  "email": "jashu@gmail.com",
  "is_active": true
}
```

Expected:

```text
Doctor created successfully
```

---

## Test 2: Invalid Doctor Email

Use:

```json
{
  "name": "Dr. Jaswanth",
  "specialization": "Cardiology",
  "email": "jashu123",
  "is_active": true
}
```

Expected:

```text
422 Unprocessable Entity
```

---

## Test 3: Create Patient

Use:

```text
POST /patients
```

Request:

```json
{
  "name": "Priya",
  "age": 20,
  "phone": "9876543210"
}
```

Expected:

```text
Patient created successfully
```

---

## Test 4: Invalid Patient Age

Use:

```json
{
  "name": "Priya",
  "age": 0,
  "phone": "9876543210"
}
```

Expected:

```text
422 Unprocessable Entity
```

---

## Test 5: Doctor Not Found

Use:

```text
GET /doctors/999
```

Expected:

```json
{
  "detail": "Doctor not found"
}
```

Status:

```text
404 Not Found
```

---

# 📋 API Summary

| Method | Endpoint               | Description       |
| ------ | ---------------------- | ----------------- |
| `POST` | `/doctors`             | Create a doctor   |
| `GET`  | `/doctors`             | List all doctors  |
| `GET`  | `/doctors/{doctor_id}` | Get doctor by ID  |
| `POST` | `/patients`            | Create a patient  |
| `GET`  | `/patients`            | List all patients |

---

# 📖 Swagger Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

FastAPI also provides ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# 💾 Data Storage

This project uses **in-memory storage** using Python lists.

Example:

```python
doctors = []
patients = []
```

Therefore, the data is temporary.

> **Note:** When the FastAPI server is restarted, previously stored doctors and patients will be lost.

---

# 📦 Submission

The project can be submitted in either of the following formats:

### Option 1: GitHub Repository

Upload the project to GitHub with:

```text
fastapi_doctor_patient/
│
├── main.py
├── requirements.txt
└── README.md
```

### Option 2: ZIP File

Compress the complete project folder into a ZIP file and submit it.

---

# 🎯 Project Objective

The main objective of this project is to understand:

* FastAPI application development
* REST API design
* HTTP methods
* API endpoints
* Pydantic models
* Data validation
* Email validation
* Error handling
* `HTTPException`
* Swagger documentation
* Uvicorn server
* In-memory data storage

---

# 👨‍💻 Author

**Jaswanth**

Python Developer / FastAPI Project

---

## ⭐ Project Status

**Completed**

The API includes Doctor and Patient management with validation and error handling.
