import datetime
from unicodedata import name
import uvicorn
import logging
import sqlite3

from fastapi import FastAPI
from fastapi.param_functions import Depends
from pydantic import BaseModel
from pydantic import BaseSettings
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.asyncio import engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from data_base.db_func import exist_table,db_insert, db_get_info
from operation.operations import check_dublicate

class Settings(BaseSettings):
    sqlite_config: str

    class Config:
        env_file = ".env"

settings = Settings()

engine = engine.create_async_engine(settings.sqlite_config, echo=True)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

#Class for post request body
class Item(BaseModel):
    name: str
    info: dict

class Add_info(BaseModel):
    name:str
    bith_date:str
    login:str 

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

@app.post('/db_write/')
async def add_info(info:Add_info ,session: AsyncSession = Depends(get_session)):
    await exist_table(session)
    if await check_dublicate(info,session):
        return "Данный пользователь уже существует"
    else:
        await db_insert(info,session)

@app.get('/db_find/{name}')
async def find_by_name(name:str,session: AsyncSession = Depends(get_session)):
    return await db_get_info(name,session)




#Starting local server 
if __name__ == "__main__":
    uvicorn.run("app_routes:app", host="0.0.0.0", port=2142, log_level="info",reload=True)