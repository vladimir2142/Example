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
    phone_number integer
    )
    """
    )
    result = await session.execute(sql_text)
    await session.commit()
    print('Сессия закрыта')
    