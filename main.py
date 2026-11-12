from fastapi import FastAPI
from pydantic  import BaseModel
from typing import List


app = FastAPI()

class Tea(BaseModel):   #usiing the BaseModel class from pydantic to create a model for the tea data
    id:int
    name: str
    origin: str
    
teas : List[Tea] = []     #using a list to store the tea data 

@app.get("/")   #using the get method to get the tea data
def get_teas1():
    return{"message":"welcome to the tea house"}
@app.get("/teas")   #using the get method to get the tea data
def get_teas():
    return teas
@app.post("/teas_post")   #using the post method to add the tea data
def add_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")   #using the put method to update the tea data
def update_tea(tea_id: int, updated_tea: Tea):
    for i,tea in enumerate(teas):
        if tea.id == tea_id:
            teas[i]=updated_tea
            return updated_tea
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")   #using the delete method to delete the tea data
def delete_tea(tea_id: int):
    for i,tea in enumerate(teas):
        if tea.id == tea_id:
            del teas[i]
            return {"message": "Tea deleted successfully"}
    return {"error": "Tea not found"}
            
        
        
    