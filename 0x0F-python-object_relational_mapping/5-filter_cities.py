#!/usr/bin/python3
"""
This is a script that lists all cities
from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         port=3306, passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    # Use binary comparison for case-sensitive search
    cur.execute("SELECT cities.id, cities.name FROM cities JOIN states ON\
        cities.state_id = states.id\
            WHERE states.name LIKE BINARY %s\
            ORDER BY cities.id ASC", (state_name,))

    rows = cur.fetchall()
    # if the row is not empty
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
