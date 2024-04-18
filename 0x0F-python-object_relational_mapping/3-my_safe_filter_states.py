#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    sns = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         port=3306, passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    # Use binary comparison for case-sensitive search
    cur.execute("SELECT * FROM states WHERE name LIKE \
        BINARY %s ORDER BY id ASC", (sns,))

    rows = cur.fetchall()

    for row in rows:
        print(row)
