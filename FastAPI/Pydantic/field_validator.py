from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str 
    age: int 
    email: EmailStr
    weight: float
    married: bool = False
    allergies: List[str]
    contact: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('age', mode='before')
    @classmethod
    def age_validator(cls, value):
        
        if 0 < value < 100: 
            return value
        else:
            raise ValueError('Age should be in 0-100')


# Corrected input data
patient_info = {
    'name': 'shravani',
    'age': '30',
    'email': 'sdfgh@hdfc.com',
    'weight': 53.3,
    'married': True,
    'allergies': ['dfghjk', 'aertyu'],
    'contact': {'mobile': '8563214523'}
}

patient_1 = Patient(**patient_info)

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

insert_patient_data(patient_1)
update_patient_data(patient_1)
