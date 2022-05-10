#!/usr/bin/python3

"""
Write a script that takes in the name of a state
as an argument and lists all  cities  of that
state, using the database  hbtn_0e_4_usa

"""
from genericpath import exists
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    cur = database.cursor()
    cur.execute("SELECT cities.name FROM cities left\
            join states on states.id = cities.state_id\
            WHERE states.name=%s order by states.id ASC;", (sys.argv[4], ))
    filas = cur.fetchall()
    larg = (len(filas))
    if larg != 0:
        for x in filas:
            larg = larg - 1
            if larg != 0:
                print(x[0], end=", ")
        print(x[0])
