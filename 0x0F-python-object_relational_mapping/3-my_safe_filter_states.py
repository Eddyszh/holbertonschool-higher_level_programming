#!/usr/bin/python3
"""Script that is safe from MySQL injections!
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    check = (argv[4], )
    cur.execute("SELECT * FROM states WHERE name = %s\
    ORDER BY states.id ASC", check)
    tbl = cur.fetchall()
    for row in tbl:
        print(row)
    cur.close()
    db.close()
