import datetime
import uvicorn
import logging

from fastapi import FastAPI
from pydantic import BaseModel

#Class for post request body
class Item(BaseModel):
    name: str
    info: dict

app = FastAPI()

@app.get('/test/{name}')
def get_request(name:str):
    """Example of get request"""
    result = {}
    result.update({'name':name,
                   'request_time':datetime.datetime.now()})
    return(result)

@app.post('/post/')
def post_request(item:Item):
    """Example of post request"""
    return item
    
#Starting local server 
if __name__ == "__main__":
    uvicorn.run("app_routes:app", host="0.0.0.0", port=2142, log_level="info",reload=True)