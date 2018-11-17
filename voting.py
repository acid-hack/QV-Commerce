import sql

SQL = sql.SQL(acid, acid_hack, Amazon)


def voting(self, uid, pid):

    x = int(input("How do you score this product? "))

    if x <= int( tokens_remaining() ):
        SQL.vote(uid, pid, x^2)

    while x > int( tokens_remaining(uid) ):
        x = int(input("You don't have the required number of tokens for such a score. Please try again "))

        if x <= int( tokens_remaining( uid )):
            SQL.vote ( uid, pid, x^2 )

            break
    return x , uid, pid



