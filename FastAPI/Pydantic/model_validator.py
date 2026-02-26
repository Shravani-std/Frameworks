from pydantic import BaseModel, EmailStr, field_validator, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str 
    age: int 
    email: EmailStr
    weight: float
    married: bool = False
    allergies: List[str]
    contact: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact:
            raise ValueError("Patients above 60 must have an emergency contact.")
        return self

# Corrected input data
patient_info = {
    'name': 'shravani',
    'age': 85,
    'email': 'sdfgh@hdfc.com',
    'weight': 53.3,
    'married': True,
    'allergies': ['dfghjk', 'aertyu'],
    'contact': {
        'mobile': '8563214523',
        'emergency': '6541239652'
    }
}

# Creating Patient instance
patient_1 = Patient(**patient_info)

# Functions
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')
    if patient.age > 60:
        emergency_contact = patient.contact.get("emergency")
        print(f"It's an emergency case, contact emergency no.: {emergency_contact}")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

# Usage
insert_patient_data(patient_1)
update_patient_data(patient_1)
