from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str 
    age: int 
    email: EmailStr
    weight: float  # in kg
    height: float  # in cm
    married: bool = False
    allergies: List[str]
    contact: Dict[str, str]

    @computed_field
    @property
    def _calculate_bmi(self) -> float:
        height_m = self.height / 100  # convert cm to meters
        bmi = round(self.weight / (height_m ** 2), 2)
        return bmi


# Input data
patient_info = {
    'name': 'shravani',
    'age': 30,
    'email': 'sdfgh@hdfc.com',
    'weight': 53.3,
    'height': 155.6,  # cm
    'married': True,
    'allergies': ['dfghjk', 'aertyu'],
    'contact': {'mobile': '8563214523'},
}

patient_1 = Patient(**patient_info)

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("BMI:", patient._calculate_bmi)
    print('inserted')

# def update_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print('updated')

insert_patient_data(patient_1)
# update_patient_data(patient_1)
