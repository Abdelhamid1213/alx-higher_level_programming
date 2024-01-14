#!/usr/bin/python3
"""
This script connects to a MySQL server and retrieves and displays states from
the 'states' table.
The results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys


def select_states(username, password, database):
    """
    Connect to MySQL server and retrieve states from the 'states' table.

    :param username: MySQL username
    :param password: MySQL password
    :param database: MySQL database name
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Main function to handle command-line arguments and execute the script.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    select_states(username, password, database)
