#!/usr/bin/python3
# Lists all atates from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>

import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    [print(state) for state in cur.fetchall()]
