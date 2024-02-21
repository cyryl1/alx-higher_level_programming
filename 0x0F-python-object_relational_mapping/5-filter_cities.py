#!/usr/bin/python3
"""
To print cities of a state passed as an argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM `cities` as `c`\
            JOIN `states` as `s`\
            ON `c`.`state_id` = `s`.`id`\
            ORDER BY `c`.`id`")
    cursor.execute(query)
    print(", ".join([city[2] for city in cursor.fetchall() if city[4] == sys.argv[4]]))
