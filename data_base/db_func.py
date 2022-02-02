from pydantic import BaseSettings
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.asyncio import engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import text



async def create_table(session:AsyncSession):
    sql_text = text( """
    CREATE table friends (
    id integer primary key,
    name text,
    bith_date text,
    login text
    )
    """
    )
    result = await session.execute(sql_text)
    await session.commit()

async def exist_table(session:AsyncSession):

    tables  = await session.execute('SELECT name from sqlite_master where type= "table"')
    if len(tables.all())>=1:
        print('table exist')
    else:
        print("table doesn't exist")
        await create_table(session)

    await session.commit()

async def db_insert(info,session:AsyncSession):
    sql_text =f"""
    INSERT INTO friends(name,bith_date,login) VALUES(
    '{info.name}',
    '{info.bith_date}',
    '{info.login}'
    )
    """
    await session.execute(sql_text)
    await session.commit()

async def db_get_info(name,session:AsyncSession):
    sql_text = f"""
    SELECT name,bith_date,login from friends where name='{name}' 
    """
    result = await session.execute(sql_text)
    await session.commit()
    return result.all()