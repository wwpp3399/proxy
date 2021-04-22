import pymysql


class MyDb:
    def __init__(self):
        self.pysql_db = pymysql.connect(host="139.196.227.121",
                                        port=3306,
                                        user="root",
                                        passwd="hu697693",
                                        charset="utf8mb4",
                                        database="soul")
        self.cursor = self.pysql_db.cursor(cursor=pymysql.cursors.DictCursor)

