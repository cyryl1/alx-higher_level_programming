#!/usr/bin/python3
import MySQLdb
"""Defines a database"""
import sys

if __name__ == "__main__":
    """ Check if the correct number of command-line arguments is provided"""
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    """Extract MySQL credentials from command-lne arguments"""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    """Establish a connection to the MySQL server"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )

    """The cursor object to interact with the database"""
    cur = db.cursor()

    """Executes the SQL query to retrieve the states"""
    query = cur.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetches all the rows"""
    all_states = cur.fetchall()

    """Display result"""
    for state in all_states:
        print(state)

    """Closes the cursor and databse connection"""
    cur.close()
    db.close()
