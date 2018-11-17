import MySQLdb

class SQL:
    def __init__(self, user, passwd, db):
        self._db = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=db, charset='utf8mb4')
        self._db.autocommit(True)
        self._cur = self._db.cursor()

    def close(self):
        self._cur.close()
        self._db.close()
