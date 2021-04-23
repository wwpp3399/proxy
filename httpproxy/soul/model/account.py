from httpproxy.soul.model.soul_account import MyDb
import time


def query_account_info_by_phone(phone: str):
    db = MyDb()
    try:
        query_sql = f"select * from account where phone='{phone}'"
        db.cursor.execute(query_sql)
        data_info = db.cursor.fetchone()
        return data_info
    except Exception as e:
        print(e)
        db.pysql_db.rollback()
        return False

    finally:
        db.cursor.close()
        db.pysql_db.close()


def query_account_info_by_smid(smid: str):
    db = MyDb()
    try:
        query_sql = f"select * from account where smDeviceId='{smid}'"
        db.cursor.execute(query_sql)
        data_info = db.cursor.fetchone()
        return data_info
    except Exception as e:
        print(e)
        db.pysql_db.rollback()
        return False

    finally:
        db.cursor.close()
        db.pysql_db.close()


def query_account_info(phone: str, smdeviceid: str):
    db = MyDb()
    try:
        query_sql = f"select * from account where phone='{phone}' and smDeviceId='{smdeviceid}'"
        db.cursor.execute(query_sql)
        data_info = db.cursor.fetchone()
        print("oooooooooooooooooooooooooooooooooooooooooooooooooo")
        return data_info
    except Exception as e:
        print(e)
        db.pysql_db.rollback()
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()


def update_login_time(phone: str):
    db = MyDb()
    try:

        update_sql = f"UPDATE account SET ltlgDate={int(time.time())} " \
                     f"WHERE phone='{phone}' and ltlgDate IS NULL"
        db.cursor.execute(update_sql)
        db.pysql_db.commit()
        return True
    except Exception as e:
        db.pysql_db.rollback()
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()


def query_DeviceId(phoneDeviceId: str):
    db = MyDb()
    try:
        query_sql = f"select * from deviceidtable where phonedeviceid='{phoneDeviceId}' and nowsmdeviceid is not null"
        db.cursor.execute(query_sql)
        data_info = db.cursor.fetchone()
        return data_info
    except Exception as e:
        db.pysql_db.rollback()
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()


def upate_phone_by_smDeviceId(smDeviceId: str, phone: str, deviceid):
    db = MyDb()
    try:
        print("更新--------+++++----------")
        update_sql = f"update deviceidtable set phone='{phone}',nowsmdeviceid='{smDeviceId}' where phonedeviceid='{deviceid}'"
        db.cursor.execute(update_sql)
        db.pysql_db.commit()
        return True

    except Exception as e:
        print(e)
        db.pysql_db.rollback()
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()


def update_by_smDeviceId(smDeviceId: str):
    db = MyDb()
    try:
        query_sql = "update deviceidtable set phone=%s,nowsmdeviceid=%s where nowsmdeviceid=%s"
        db.cursor.execute(query_sql, (None, None, smDeviceId))
        db.pysql_db.commit()
        print("更新当前设备为NULL成功")
        return True
    except Exception as e:
        print('更新失败')
        db.pysql_db.rollback()
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()


def query_device_info_by(nowsmdeviceid: str, phone: str):
    db = MyDb()
    try:
        query_sql = f"select * from deviceidtable where phone='{phone}' and nowsmdeviceid='{nowsmdeviceid}'"
        db.cursor.execute(query_sql)
        device_info = db.cursor.fetchone()
        return device_info
    except Exception as e:
        db.pysql_db.rollback()
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()


def add_deviceid_info(phonedeviceid: str):
    db = MyDb()
    try:
        insert_sql = f"insert into deviceidtable(phonedeviceid) values ('{phonedeviceid}')"
        db.cursor.execute(insert_sql)
        db.pysql_db.commit()
        return True
    except Exception as e:
        db.pysql_db.rollback()
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()
