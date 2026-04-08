# Pydantics AfterValidation inside of Annotated
from fastapi import FastAPI, Query, Path
from typing import Annotated
from pydantic import AfterValidator

import random

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_if_validate(id : str):
    if not id.startswith( ("isbn-", "imbd-") ):
        raise ValueError("Invalid ID Formate.....")
    return id

@app.post("/add_items")
async def add_item(
    id: Annotated[str | None, AfterValidator(check_if_validate)] = None,
    name: Annotated[str , Query(min_length=5, max_length=50)] = None,
    
):
    data[id] = name
    return {
        "msg": "Item Added",
        "data": data[id]
    }



@app.get("/items")
async def read_items(
    id : Annotated[str | None, AfterValidator(check_if_validate)] = None
):
    if id:
        item = data.get(id)
    else:
        id , item = random.choice(list(data.items()))
    return {
        "id" : id,
        "name" : item
    }

@app.get("/items/{id}")
async def get_item(
    id: Annotated[int , Path(title="The ID of item to get") ],
    name : Annotated[str | None, Query(alias="item-query")] = None
):
    results = {"id" : id}
    if name:
        results.update( {"q" : name} )

    return results