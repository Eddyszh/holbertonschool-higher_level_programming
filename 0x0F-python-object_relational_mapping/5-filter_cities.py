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
    cur.execute("SELECT * FROM cities JOIN states\
    ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC", check)
    tbl = cur.fetchall()
    cities = []
    for row in tbl:
        if row[4] == check[0]:
            cities.append(row[2])
    print(', '.join(cities))
    cur.close()
    db.close()
