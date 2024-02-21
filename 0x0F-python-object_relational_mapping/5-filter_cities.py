#!/usr/bin/python3
"""
To print cities of a state passed as an argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT `c`.`name`\
            FROM `cities` as c\
            JOIN `states` as s\
            ON `c`.`state_id` = `s`.`id`\
            WHERE BINARY `s`.`name` = '{}'\
            ORDER BY `c`.`id`".format(sys.argv[4])
    cursor.execute(query)
    [print(", ".join(city)) for city in cursor.fetchall()]
