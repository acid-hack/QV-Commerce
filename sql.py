import MySQLdb

class SQL:
    def __init__(self, user, passwd, db):
        """
        Creates a database connection
        :param user: User used to connect to the database
        :param passwd: Password for the user to connect to the database
        :param db: Database name
        """
        self._db = MySQLdb.connect(host='localhost', user=user, passwd=passwd, db=db, charset='utf8mb4')
        self._db.autocommit(True)
        self._cur = self._db.cursor()

    def close(self):
        """
        Closes the database connection
        :return:
        """
        self._cur.close()
        self._db.close()
