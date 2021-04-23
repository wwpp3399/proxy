from httpproxy.soul.model.soul_account import MyDb


def query_phone_info(phone: str):
    db = MyDb()
    sql = f"select * from account where phone={phone}"
    db.cursor.execute(sql)
    data_soul = db.cursor.fetchone()
    # db.cursor.close()
    # db.pysql_db.close()
    # print(data_soul)
    return data_soul

# query_phone_info("15137107150")
