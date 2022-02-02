from sqlalchemy import false
from data_base.db_func import db_get_info

async def check_dublicate(info,session):
    db_reqiest = await db_get_info(info.name,session)
    print(db_reqiest, info)
    if len(db_reqiest)>=1:
        for x in db_reqiest:
            if x['login'] ==info.login and x['bith_date']==info.bith_date:
                return True
        return False
    else:
        return False    
        