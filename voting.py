from sql import SQL

sql = SQL('acid', 'acid_hack', 'Amazon')


def voting(self, uid, pid):

    x = int(input("How do you score this product? "))

    if x <= int( sql.tokens_remaining(uid) ):
        sql.vote(uid, pid, x^2)

    while x > int( sql.tokens_remaining(uid) ):
        x = int(input("You don't have the required number of tokens for such a score. Please try again "))

        if x <= int( sql.tokens_remaining( uid )):
            sql.vote( uid, pid, x^2 )

            break
    return x , uid, pid



