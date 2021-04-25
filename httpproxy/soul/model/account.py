from httpproxy.soul.model.soul_account import MyDb
import time


def query_account_info_by_phone(phone: str):
    db = MyDb()
    try:
        query_sql = f"select * from account where phone='{phone}'"
        db.cursor.execute(query_sql)
        data_info = db.cursor.fetchone()
        # print("数据库查取手机号注册信息----获得token成功------------------")
        return data_info
    except Exception as e:
        print(e)
        # print("数据库查取手机号注册信息----获得token失败------------------")
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
        # print(e)
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
        # print("oooooooooooooooooooooooooooooooooooooooooooooooooo")
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

        update_sql = f"UPDATE account SET ltlgDate={int(time.time())} WHERE phone='{phone}' and ltlgDate IS NULL"
        db.cursor.execute(update_sql)
        db.pysql_db.commit()
        # print("更新成功")
        return True
    except Exception as e:
        # print("更新失败")
        db.pysql_db.rollback()
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()

def query_DeviceId_bool(phoneDeviceId: str):
    db = MyDb()
    try:
        query_sql = f"select * from deviceidtable where phonedeviceid='{phoneDeviceId}'"
        db.cursor.execute(query_sql)
        data_info = db.cursor.fetchone()
        # print("数据库查到start_smDeviceId----成功------------------")
        return data_info
    except Exception as e:
        db.pysql_db.rollback()
        # print("数据库查到start_smDeviceId----失败------------------")
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()


def upate_phone_by_smDeviceId(smDeviceId: str, phone: str, deviceid):
    db = MyDb()
    try:
        print("更新--------device表字段信息+++----------")
        update_sql = f"update deviceidtable set phone='{phone}',nowsmdeviceid='{smDeviceId}' where phonedeviceid='{deviceid}'"
        db.cursor.execute(update_sql)
        db.pysql_db.commit()
        # print("更新账号信息成功----------------------")
        return True

    except Exception as e:
        print(e)
        # print("更新账号信息---失败----------------------")
        db.pysql_db.rollback()
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()


def delete_device_by_smDeviceId(smDeviceId: str):
    db = MyDb()
    try:
        query_sql = f"delete from deviceidtable where nowsmdeviceid='{smDeviceId}'"
        db.cursor.execute(query_sql)
        db.pysql_db.commit()
        # print("删除当前设备成功")
        return True
    except Exception as e:
        # print('删除失败')
        db.pysql_db.rollback()
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()


def query_now_sm_device_id_info(nowsmdeviceid:str):
    db = MyDb()
    try:
        query_sql = f"select * from deviceidtable where nowsmdeviceid='{nowsmdeviceid}'"
        db.cursor.execute(query_sql)
        device_info = db.cursor.fetchone()
        # print("数据库查取手机号跟注册sm_deviceId----成功------------------")
        return device_info
    except Exception as e:
        print(e)
        # print("数据库查取手机号跟注册sm_deviceId----失败------------------")
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
        # print("插入start_smDeviceId成功")
        return True
    except Exception as e:
        db.pysql_db.rollback()
        # print("插入start_smDeviceId失败")
        return False
    finally:
        db.cursor.close()
        db.pysql_db.close()
