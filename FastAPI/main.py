from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json 
app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of Patient', examples=['P001'])]
    name: Annotated[str, Field(...,description='Name of the Patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the Patient')]
    gender: Annotated[Literal['male','female','others'], Field(..., description='Gender of the Patient')]
    
    height: Annotated[float, Field(..., gt=0,  description='Height of the Patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='weight of the Patient in kgs')]
    # bmi = float
    # verdict = str
    @computed_field
    @property
    def bmi(self) ->float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
    


    @computed_field
    @property
    def verdict(self) ->str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25 or self.bmi < 30:
            return 'Normal'
        else:
            return 'Overweight'
        
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Literal['male','female','others'], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

#dataloading
def load_data():
    with open('E:\AI\FastAPI\patients.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('E:\AI\FastAPI\patients.json', 'w') as f:
        json.dump(data,f)


@app.get("/")
def hello():
    return {'message':'Patient management system API'}

@app.get('/about')
def about():
    return {'message': ' A fully functional API to manage your patient record'}

@app.get('/view')
def view():
    data = load_data()

    return data


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in DB', example='patient_12')):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient Not Found')
    # return {'error': 'patient not found'}


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data



@app.post('/create')
def create_patient(patient: Patient):
    #load_data()
    data = load_data()


    # check if patient already exist
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already present')
    
    #new Patient add to the db
    data[patient.id] = patient.model_dump(exclude= ['id'] )

    #save in json formate
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'Patient created successfully'} )



@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate ):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient Not found')
    
    existing_patient_info = data[patient_id]

    updated_Patient_info = patient_update.model_dump(exclude_unset=True) #only particular paras were selected 


    for key, value in updated_Patient_info.items():
        existing_patient_info[key] = value
    
    # existing_patient_info -> pydantic object => updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)
    # pydantic obj -> dictionary
    existing_patient_info = patient_pydantic_obj.model_dump(exclude='id')

    data[patient_id] = existing_patient_info


    save_data(data)
    return JSONResponse(status_code=201, content={'message': 'Patient Updated successfully'} )


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient Not found')
    del data[patient_id]

    save_data(data)
    return JSONResponse(status_code=200, content={'message': 'Patient Deleted successfully'} )
