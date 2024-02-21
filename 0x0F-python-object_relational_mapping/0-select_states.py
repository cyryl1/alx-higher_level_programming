#!/usr/bin/python3
"""
To list all the state in a table states
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in cursor.fetchall()]
