import bcrypt
import MySQLdb
import time
import uuid


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

    def create_fresh(self):
        """
        Creates a fresh AccountInfo and ProductInfo tables
        :return:
        """
        #Account Info
        self._cur.execute('DROP TABLE IF EXISTS `AccountInfo`')
        q = 'CREATE TABLE `AccountInfo` ('
        columns = ['`uid` CHAR(33) UNIQUE',
                   '`email` VARCHAR(254) UNIQUE',
                   '`passwd` CHAR(128)',
                   '`orders` INT UNSIGNED',
                   '`products_voted` INT UNSIGNED',
                   '`tokens_remaining` INT UNSIGNED',
                   '`tokens_spent` INT UNSIGNED',
                   '`last_updated` INT UNSIGNED']
        for c in columns:
            q += c+', '
        q = q[:-1]
        q += ') ENGINE=InnoDB'
        self._cur.execute(q)

        #Product Info
        self._cur.execute('DROP TABLE IF EXISTS `ProductInfo`')
        q = 'CREATE TABLE `ProductInfo` ('
        columns = ['`pid` CHAR(33) UNIQUE',
                   '`total_votes` INT UNSIGNED',
                   '`total_positive_votes` INT UNSIGNED',
                   '`total_negative_votes` INT UNSIGNED',
                   '`average_vote` FLOAT(10,5)',
                   '`stddv_vote`, FLOAT(10,5)',
                   '`votes_sum` BIGINT UNSIGNED']
        for c in columns:
            q += c+', '
        q = q[:-1]
        q += ') ENGINE=InnoDB'
        self._cur.execute(q)

    def populate_random(self):
        """
        Populates account info table with random data
        :return:
        """
        return

    def check_login(self, email, passwd):
        """
        Checks whether email and passwd are valid
        :param email:
        :param passwd:
        :return bool: True if email and passwd are valid
        """
        q = 'SELECT `passwd` FROM `AccountInfo` WHERE `email`=%s'
        tup = (email, )
        self._cur.execute(q, tup)
        real_passwd = ''
        for row in self._cur.fetchall():
            real_passwd = row[0]
        real_passwd = bytes(real_passwd, 'utf-8')
        if bcrypt.checkpw(passwd, real_passwd):
            return True
        return False

    def get_uid(self, email):
        """
        Gets the uid that corresponds to the email
        :param email:
        :return str: uid
        """
        q = 'SELECT `uid` FROM `AccountInfo` WHERE `email`=%s'
        tup = (email, )
        uid = None
        self._cur.execute(q, tup)
        for row in self._cur.fetchall():
            uid = row[0]
        return uid

    def register(self, email, passwd, rounds=10):
        """
        Registers a new user
        :param email:
        :param passwd:
        :param rounds: Difficulty of hash algorithm
        :return bool: False if a user already exists
        """
        uid = self.get_uid(email)
        if uid is not None:
            return False
        passwd = bytes(passwd, 'utf-8')
        hashed_pw = bcrypt.hashpw(passwd, bcrypt.gensalt(rounds))
        q = 'INSERT INTO `AccountInfo` '
        q += '(`uid`, `email`, `passwd`, `orders`, `products_voted`, `tokens_remaining`, `tokens_spent`, `last_updated`)'
        q += ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        uid = str(uuid.uuid4())
        uid = 'u'+uid.replace('-', '')
        t = int(time.time())
        tup = (uid, email, hashed_pw, 0, 0, 0, 0, t)
        self._cur.execute(q, tup)
        return True

    def register_product(self, pid):
        """
        Creates table for pid
        Adds row in ProductInfo table for pid
        :param pid: Product id
        :return:
        """
        #make pid
        pid = str(uuid.uuid4())
        pid = 'p' + pid.replace('-', '')

        #create table
        self._cur.execute('DROP TABLE IF EXISTS `ProductInfo`')
        q = 'CREATE TABLE `%s` (`uid` CHAR(33), `votes` INT UNSIGNED, `time` INT UNSIGNED) ENGINE=InnoDB'
        self._cur.execute(q)

        #add row
        q = 'INSERT INTO `ProductInfo` '
        q += '(`pid`, `total_votes`, `total_positive_votes`, `total_negative_votes`, `average_vote`, `stddv_vote`, `votes_sum`)'
        q += ' VALUES (%s, 0, 0, 0, 0, 0, 0)'
        tup = (pid, )
        self._cur.execute(q, tup)

    def tokens_remaining(self, uid):
        """
        Checks how many tokens the user has remaining
        :param uid:
        :return int: Tokens remaining
        """
        tokens = None
        q = 'SELECT `tokens_remaining` FROM `AccountInfo` WHERE `uid`=%s' % uid
        self._cur.execute(q)
        for row in self._cur.fetchall():
            tokens = row[0]
        return tokens

    def vote(self, uid, pid, cost):
        """
        Votes using the cost passed (which is subtracted from tokens_remaining)
        Updates products_voted, tokens_remaining, tokens_spent, and last_updated
        Does NOT check that you have enough tokens, and will likely raise an error if you don't
        :param uid: User id
        :param pid: Product id
        :param cost: Number of tokens to be removed
        :return:
        """
        

    def close(self):
        """
        Closes the database connection
        :return:
        """
        self._cur.close()
        self._db.close()
