from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(
    title="Doctor and Patient Management API",
    description="Simple REST API using FastAPI",
    version="1.0.0"
)

# Pydantic Models

class Doctor(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


class Patient(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str

# In-memory storage

doctors = []
patients = []

doctor_id_counter = 1
patient_id_counter = 1

# Doctor APIs

@app.post("/doctors")
def create_doctor(doctor: Doctor):
    global doctor_id_counter

    new_doctor = {
        "id": doctor_id_counter,
        "name": doctor.name,
        "specialization": doctor.specialization,
        "email": doctor.email,
        "is_active": doctor.is_active
    }

    doctors.append(new_doctor)
    doctor_id_counter += 1

    return {
        "message": "Doctor created successfully",
        "doctor": new_doctor
    }


@app.get("/doctors")
def get_doctors():
    return {
        "message": "Doctors retrieved successfully",
        "doctors": doctors
    }


@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):

    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor

    raise HTTPException(
        status_code=404,
        detail="Doctor not found"
    )


# Patient APIs

@app.post("/patients")
def create_patient(patient: Patient):
    global patient_id_counter

    new_patient = {
        "id": patient_id_counter,
        "name": patient.name,
        "age": patient.age,
        "phone": patient.phone
    }

    patients.append(new_patient)
    patient_id_counter += 1

    return {
        "message": "Patient created successfully",
        "patient": new_patient
    }


@app.get("/patients")
def get_patients():
    return {
        "message": "Patients retrieved successfully",
        "patients": patients
    }
