#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM `states`"
    cursor.execute(query)
    [print(state) for state in cursor.fetchall() if state[1] == sys.argv[4]]
