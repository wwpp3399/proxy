import pymysql


class MyDb:
    def __init__(self):
        self.pysql_db = pymysql.connect(host="39.103.174.179",
                                        port=3306,
                                        user="root",
                                        passwd="hu697693",
                                        charset="utf8mb4",
                                        database="soul")
        self.cursor = self.pysql_db.cursor(cursor=pymysql.cursors.DictCursor)

    def db_close(self):
        self.cursor.close()
        self.pysql_db.close()
# class MyDb:
#
#     @classmethod
#     def instance(cls):
#         if not hasattr(MyDb, "_instance"):
#             cls.pysql_db = pymysql.connect(host="139.196.227.121",
#                                            port=3306,
#                                            user="root",
#                                            passwd="hu697693",
#                                            charset="utf8mb4",
#                                            database="soul")
#             cls.cursor = cls.pysql_db.cursor(cursor=pymysql.cursors.DictCursor)
#             MyDb._instance = MyDb()
#         return MyDb._instance
#
#     @classmethod
#     def clear_instance(cls):
#
#         del cls.instance

# class MyDb:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'_instance'):
#             cls.obj = super().__new__(cls)
#         return cls.obj
#
#     def __init__(self):
#         self.pysql_db = pymysql.connect(host="139.196.227.121",
#                                                    port=3306,
#                                                    user="root",
#                                                    passwd="hu697693",
#                                                    charset="utf8mb4",
#                                                    database="soul")
#         self.cursor = self.pysql_db.cursor()
#
#     def __del__(self):
#         self.cursor.close()
#         self.pysql_db.close()
