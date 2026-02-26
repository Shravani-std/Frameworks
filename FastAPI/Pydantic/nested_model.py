from pydantic import BaseModel

#for complex variables like address we made new pydantic model
class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address #complex data made with different attributes

address_dict = {'city': 'gurgaon','state':'Haryana','pin':'70'}
address_1 = Address(**address_dict)

patient_dict = {
    'name':'Shravani',
    'gender':'Female',
    'age':85,
    'address': address_1
    }
patient1 = Patient(**patient_dict)

print(patient1)
print("Patient City: ", patient1.address.city)

temp = patient1.model_dump()
temp1 = patient1.model_dump_json()
print("Every details of Patient: ", temp)
print(type(temp))
print("Every details of Patient(JSON): ", temp1)
print(type(temp1))

temp2 = patient1.model_dump(exclude={'address':['state']})   #deleted the state 
print(temp2)

temp2 = patient1.model_dump(exclude_unset=True)   #exclude_unset=True tells Pydantic to exclude any fields that were not set when the model was created.