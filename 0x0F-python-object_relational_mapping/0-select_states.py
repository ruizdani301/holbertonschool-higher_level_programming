#!/usr/bin/python3
"""
 lists all  states  from the database  hbtn_0e_0_usa

"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = database.cursor()
    cur.execute("SELECT * FROM states order by states.id ASC;")
    filas = cur.fetchall()
    for x in filas:
        print(x)
