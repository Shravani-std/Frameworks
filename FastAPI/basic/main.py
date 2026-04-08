from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
from enum import Enum

class Item(BaseModel):
    name: str = None
    is_done : bool = False

@app.get('/')
def root():
    return {
        'msg': "Hello World"
    }
@app.get('/name')
def name():
    return{
        'name': "Shravani Tingare"
    }
items = [] 

@app.post('/items', response_model=list[Item])
def addItems(item:Item): #path parameter
    items.append(item)
    return items

@app.get("/item/{item_id}", response_model=Item)
def see_item(item_id:int) -> Item:
    item = items[item_id]
    return item


# Using 'enum'
class ModelName(str, Enum):
    ResNet =  'ResNet'
    lenet = 'lenet'
    alexNet = 'alexNet'
@app.get('/models/{model_name}')
async def get_model(model_name:ModelName):
    if model_name is ModelName.lenet:
        return{
            "model_name": model_name,
            "msg" : "model_2"
        }
    elif model_name is ModelName.alexNet:
        return{
            "model_name":model_name,
            "msg": "model_3"
    
          }
    else:
        return{
            "model_name": model_name,
            "msg": "Model_1"
        }
    
# enum + BaseModel
# enum: Restricts the values of variable
# baseModel: Data validation, Data parsing , Clean Data Structure
class Status(str, Enum):
    pending="Pending"
    complete="Complete"
    cacelled="cancelled"
class Order(BaseModel):
    status:Status