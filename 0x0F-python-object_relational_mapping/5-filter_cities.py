#!/usr/bin/python3

"""
Write a script that takes in the name of a state
as an argument and lists all  cities  of that
state, using the database  hbtn_0e_4_usa

"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    cur = database.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities left\
            join states on states.id = cities.state_id\
            WHERE states.name=%s order by states.id ASC;", (sys.argv[4], ))
    filas = cur.fetchall()
    for x in filas:
        print(x)
