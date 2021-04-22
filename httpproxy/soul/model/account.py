from httpproxy.soul.model.soul_account import MyDb


def query_phone_info(phone: str):
    db = MyDb()
    sql = f"select * from account where phone={phone}"
    db.cursor.execute(sql)
    data_soul = db.cursor.fetchone()
    db.cursor.close()
    db.pysql_db.close()
    return data_soul

