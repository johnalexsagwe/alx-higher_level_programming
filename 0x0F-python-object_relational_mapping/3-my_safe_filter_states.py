#!/usr/bin/python3


"""
Filter states
"""


import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER\
            BY id ASC",
        (sys.argv[4],),
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close
