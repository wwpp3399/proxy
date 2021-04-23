import pymysql


class MyDb:

    @classmethod
    def instance(cls):
        if not hasattr(MyDb, "_instance"):
            cls.pysql_db = pymysql.connect(host="139.196.227.121",
                                        port=3306,
                                        user="root",
                                        passwd="hu697693",
                                        charset="utf8mb4",
                                        database="soul")
            cls.cursor = cls.pysql_db.cursor(cursor=pymysql.cursors.DictCursor)
            MyDb._instance = MyDb()
        return MyDb._instance

    @classmethod
    def clear_instance(cls):
        del cls.instance


# ins =  MyDb.instance()
# ins.clear_instance()
# print(ins)