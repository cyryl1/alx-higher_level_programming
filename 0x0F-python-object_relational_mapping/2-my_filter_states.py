#!/usr/bin/python3

import sys
import MySQLdb

"""
This module provides a function to list all states in the hbtn_0e_0_usa database.
"""

def list_states(user, password, database, state):
    """
    Lists all states in the hbtn_0e_0_usa database in ascending order by id.

    Args:
        user (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.
        state (str): Name of state

    Returns:
        None
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query, (state,))

    # Fetch and print all rows in the result
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    """
    Main function to list all states in the hbtn_0e_0_usa database.

    Args:
        None

    Returns:
        None
    """
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    list_states(user, password, database, state)
