# Doctor and Patient Management API

A simple REST API built using **Python and FastAPI** to manage doctors and patients.

This project demonstrates REST API development, Pydantic validation, error handling, and in-memory data storage.

---

##  Technologies Used

* Python 3.9+
* FastAPI
* Pydantic
* Uvicorn
* Email Validator
* In-memory storage

---

##  Project Structure

```text
fastapi_doctor_patient/
│
├── main.py
├── requirements.txt
└── README.md
```

---

#  Installation and Setup

## Step 1: Check Python

Open Command Prompt and run:

```bash
python --version
```

Python version should be **3.9 or above**.

---

## Step 2: Open the Project Folder

Open Command Prompt and go to your project folder.

Example:

```bash
cd Desktop\fastapi_doctor_patient
```

---

## Step 3: Install Required Packages

Run:

```bash
pip install fastapi uvicorn email-validator
```

Or install using the requirements file:

```bash
pip install -r requirements.txt
```

---

#  Run the Application

Run the following command:

```bash
python -m uvicorn main:app --reload
```

You should see:

```text
Uvicorn running on http://127.0.0.1:8000

---

For testing the APIs, open the FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test all API endpoints directly from the browser.

---

#  Doctor APIs

## 1. Create Doctor

### Endpoint

```text
POST /doctors
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



---

## 2. Get All Doctors

### Endpoint

```text
GET /doctors
```


---

## 3. Get Doctor by ID

### Endpoint

```text
GET /doctors/{doctor_id}
```

Example:

```text
GET /doctors/1
```


---

#  Patient APIs

## 1. Create Patient

### Endpoint

```text
POST /patients
```

### Request Body

```json
{
  "name": "Priya",
  "age": 20,
  "phone": "9876543210"
}
```



---

## 2. Get All Patients

### Endpoint

```text
GET /patients
```


---

#  Validation

The application uses **Pydantic models** for data validation.

## Email Validation

Doctor email must be a valid email address.

Valid:

```text
jashu@gmail.com
```

Invalid:

```text
jashu123
```

The model uses:

```python
email: EmailStr
```

Invalid email data will return a **422 Unprocessable Entity** error.

---

## Age Validation

Patient age must be greater than 0.

Valid:

```text
20
```

Invalid:

```text
0
-5
```

The model uses:

```python
age: int = Field(gt=0)
```

If the age is 0 or negative, FastAPI returns a **422 Unprocessable Entity** error.

---

#  Error Handling

The application uses `HTTPException` for errors.

For example, if a doctor does not exist:

```text
GET /doctors/999
```

Response:

```json
{
  "detail": "Doctor not found"
}
```

Status code:

```text
404 Not Found
```

The application also automatically handles validation errors using FastAPI and Pydantic.

---


---

#  API Summary

| Method | Endpoint               | Description       |
| ------ | ---------------------- | ----------------- |
| POST   | `/doctors`             | Create a doctor   |
| GET    | `/doctors`             | List all doctors  |
| GET    | `/doctors/{doctor_id}` | Get doctor by ID  |
| POST   | `/patients`            | Create a patient  |
| GET    | `/patients`            | List all patients |

---

