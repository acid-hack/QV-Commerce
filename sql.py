import bycrypt
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

    def create_fresh(self):
        """
        Creates a fresh AccountInfo table
        :return:
        """
        q = "CREATE TABLE `AccountInfo` (uid CHAR(33) UNIQUE, email VARCHAR(254) UNIQUE, passwd CHAR(128), orders INT UNSIGNED, products_voted INT UNSIGNED, tokens_remaining INT UNSIGNED, tokens_spent INT UNSIGNED, last_updated INT UNSIGNED) ENGINE=InnoDB"

    def populate_acc_info(self):
        """
        Populates account info table with random data
        :return:
        """

    def check_login(self, email, passwd):
        """
        Checks whether email and passwd are valid
        :param email:
        :param passwd:
        :return bool: True if email and passwd are valid
        """
        q = "SELECT "
    
    def get_uid(self, email):
        """
        Gets the uid that corresponds to the email
        :param email: 
        :return str: uid 
        """
        q = ""

    def register(self, email, passwd):
        """
        Registers a user
        :param email:
        :param passwd:
        :return bool: False if user already exists
        """
        return

    def tokens_remaining(self, uid):
        """
        Checks how many tokens the user has remaining
        :param uid:
        :return int: Tokens remaining
        """

    def vote(self, tokens):
        """
        Votes using however many tokens were passed
        Updates products_voted, tokens_remaining, tokens_spent, and last_updated
        Does NOT check that you have enough votes, and will raise an error if you don't
        :param tokens: Number of tokens to vote with
        :return:
        """

    def close(self):
        """
        Closes the database connection
        :return:
        """
        self._cur.close()
        self._db.close()
