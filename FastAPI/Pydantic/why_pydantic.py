from pydantic import BaseModel, EmailStr, AnyUrl, Field #Meta data can be use and attached
from typing import List, Dict, Optional, Annotated

#step-1 : Pydantic model were we've defined the schemas
class Patient(BaseModel):
    name: str = Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title='qwertyuioplkjhgfdszxcvbnm [poiuytrewasdfghjk,mnbvcxz', description='riguhriugiurdgndfnhir righni rignhtionhrt o9iogijhftoih 9i9jtrhiurty', examples=['shravani', "sameer"])]
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    linked_in_url: AnyUrl
    weight: float = Field(gt=0)    #coz of Field we can declare condition and can apply it
    married: bool = False
    married: Annotated[bool, Field(default=None, description='sdfghjsdfgerf gertg hrt hrfgh')]
    allergies: Optional[List[str]] = None # default 
    allergies: Optional[List[str]] = Field(max_length=10) # default 
    contact = Dict[str,str]


#STEP-2: making objects
patient_info = {'name': 'shravani', 'age':'30','weight': 53.3,'married':True, 'allergies':['dfghjk','aertyu'], 'contact': 8563214523}
patient_1 = Patient(**patient_info) #unpack diction **Patient_info here



def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')
    
    # if type(name) == str and type(age) == int:
    #     if age < 0:
    #         raise ValueError
    #     print(name)
    #     print(age)
    #     print('insertd into database')
    # else:
    #     raise TypeError('Incorrect datatype')

insert_patient_data(patient_1)
update_patient_data(patient_1)